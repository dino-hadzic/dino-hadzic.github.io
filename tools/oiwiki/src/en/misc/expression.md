---
title: Expression evaluation
---

The problem solved by expression evaluation is usually the following: the input is an expression given as a string, and its value must be output. Of course, there are also variants, e.g. whether the expression contains parentheses or exponentiation, how many variables it contains, whether several expressions must be checked for equivalence, and so on.

An expression usually has to be parsed first (grammar parsing) and then evaluated; it is also possible to evaluate while parsing. The role of parsing is to check whether the input string is a valid expression, and it is usually handled by a parser.

An expression contains two kinds of characters: operands and operators. For an expression of length $n$, with a suitable parsing method, parsing and evaluation can be done in $O(n)$ time.

## Expression trees and reverse Polish notation

One method of parsing an expression recursively is to parse the expression as an ordinary grammar rule, split it after parsing into the expression tree shown in the figure, and then compute bottom-up on the tree structure.![](./images/bet.png)

Performing a [tree traversal](../graph/tree-basic.md#tree-traversal) on the expression tree yields different kinds of expressions. Arithmetic expressions come in three kinds: prefix, infix and postfix expressions. Infix expressions are the ones most commonly used in everyday life; postfix expressions are the ones a computer understands easily.

-   Preorder traversal corresponds to the prefix expression (Polish notation)
-   Inorder traversal corresponds to the infix expression
-   Postorder traversal corresponds to the postfix expression (reverse Polish notation)

Reverse Polish notation (postfix notation) is a way of writing mathematical expressions in which the operator comes after its operands. For example, the following expression:

$$
a+b*c*d+(e-f)*(g*h+i)
$$

can be written in reverse Polish notation as:

$$
abc*d*+ef-gh*i+*+
$$

Therefore, reverse Polish expressions and expression trees are in one-to-one correspondence. Reverse Polish notation does not need parentheses; its order of evaluation is uniquely determined.

The convenience of reverse Polish notation is that it is very easy to evaluate in linear time. For example: in the reverse Polish expression $3~2~*~1~-$, first $3 \times 2 = 6$ is computed (using the last operator, i.e. the operator on top of the stack), and then $6 - 1 = 5$. We can see that for a reverse Polish expression it suffices to **maintain a stack of numbers; every time an operator is encountered, pop the two top elements of the stack and push the result of the operation back onto the stack**. In the end, the only element on the stack is the value of the reverse Polish expression. This algorithm has $O(n)$ time complexity.

Whether parsing an expression recursively succeeds depends on whether the grammar rules are designed sensibly, i.e. whether the desired expression tree can be obtained successfully. For example:

$$
a+b*c
$$

Because addition and multiplication have different precedence, this infix expression can be turned into two different expression trees. We can see that the design of the grammar rules depends heavily on operator precedence. Designing the corresponding recursive grammar rules based on operator precedence is in fact not an easy task.

The method introduced below treats an operator together with its precedence as a whole and parses and evaluates the expression non-recursively, directly according to operator precedence.

## Parenthesized expressions containing only left-associative binary operators

Consider a simplified problem. Assume that all operators are binary: every operator has two arguments. Also, all operators are left-associative: if operators have equal precedence, they are executed from left to right. Parentheses are allowed.

To evaluate an infix expression of this kind, we can convert it into a postfix expression and then evaluate it. Define two [stacks](../ds/stack.md) that store operators and operands respectively; whenever a number is encountered, it is put directly onto the operand stack. Each operator block corresponds to a pair of parentheses, and the operator stack is monotone only inside an operator block. Whenever an operator is encountered, we look at the elements of the topmost operator block on the operator stack and keep the operators inside the block in decreasing order of precedence by popping appropriately, computing the value of the corresponding subexpression as we pop.

In what follows, "output" means outputting to the postfix expression, i.e. putting the number onto the operand stack, or popping an operator and two operands, computing, and pushing the result back onto the operand stack. Scan the infix expression from left to right:

1.  If a number is encountered, output it directly.
2.  If a left parenthesis is encountered, put it onto the operator stack.
3.  If a right parenthesis is encountered, keep outputting the top element of the stack until a left parenthesis is encountered, and pop the left parenthesis. In other words, execute all operators inside a pair of parentheses.
4.  If any other operator is encountered, keep outputting all operators whose precedence is greater than or equal to that of the current operator. Finally, push the new operator onto the operator stack.
5.  After the whole string has been processed, some operators may still be on the stack, so output the remaining symbols from the stack one by one; the conversion of the expression is then finished.

Here is an implementation of this method for the four operators $+$, $-$, $*$, $/$:

??? note "Sample code"
    ```cpp
    
    bool delim(char c) { return c == ' '; }
    
    bool is_op(char c) { return c == '+' || c == '-' || c == '*' || c == '/'; }
    
    int priority(char op) {
      if (op == '+' || op == '-') return 1;
      if (op == '*' || op == '/') return 2;
      return -1;
    }
    
    void process_op(stack<int>& st, char op) {  // can also be used to evaluate a postfix expression
      int r = st.top();                         // pop the top elements, mind the order
      st.pop();
      int l = st.top();
      st.pop();
      switch (op) {
        case '+':
          st.push(l + r);
          break;
        case '-':
          st.push(l - r);
          break;
        case '*':
          st.push(l * r);
          break;
        case '/':
          st.push(l / r);
          break;
      }
    }
    
    int evaluate(string& s) {  // can also be adapted to convert infix to postfix
      stack<int> st;
      stack<char> op;
      for (int i = 0; i < (int)s.size(); i++) {
        if (delim(s[i])) continue;
    
        if (s[i] == '(') {
          op.push('(');  // 2. if a left parenthesis is encountered, put it onto the operator stack
        } else if (s[i] == ')') {  // 3. if a right parenthesis is encountered, execute all operators inside the pair of parentheses
          while (op.top() != '(') {
            process_op(st, op.top());
            op.pop();  // keep outputting the top of the stack until a left parenthesis is encountered
          }
          op.pop();                // pop the left parenthesis
        } else if (is_op(s[i])) {  // 4. if any other operator is encountered
          char cur_op = s[i];
          while (!op.empty() && priority(op.top()) >= priority(cur_op)) {
            process_op(st, op.top());
            op.pop();  // keep outputting all operators with precedence greater than or equal to the current one
          }
          op.push(cur_op);  // push the new operator onto the operator stack
        } else {            // 1. if a number is encountered, output it directly
          int number = 0;
          while (i < (int)s.size() && isalnum(s[i]))
            number = number * 10 + s[i++] - '0';
          --i;
          st.push(number);
        }
      }
    
      while (!op.empty()) {
        process_op(st, op.top());
        op.pop();
      }
      return st.top();
    }
    
    ```

The time complexity of this algorithm, which implicitly uses reverse Polish notation to evaluate the expression, is $O(n)$. By slightly modifying the implementation above, the reverse Polish expression can also be obtained in explicit form.

### Unary operators and right-associative operators

Now assume that the expression also contains unary operators, i.e. operators with only one argument. Unary plus and unary minus are common examples of unary operators.

One difference in this case is that we need to determine whether the current operator is unary or binary.

Note that a unary operator is usually preceded by another operator or an opening parenthesis, unless the unary operator is at the very beginning of the expression. A binary operator is always preceded by an operand or a right parenthesis. Therefore, we can keep a flag indicating whether the next operator may be unary.

In addition, unary and binary operators must be executed differently, and unary operators must have higher precedence than all binary operators. Note that some unary operators, such as unary plus and unary minus, are actually right-associative.

Right associativity means that whenever precedences are equal, the operators must be evaluated from right to left.

As mentioned above, unary operators are usually right-associative. Another example of a right-associative operator is exponentiation. The expression $a \wedge b \wedge c$ is usually interpreted as $a^{b^c}$, not $(a^b)^c$.

To handle such operators correctly, the corresponding change is to postpone popping operators from the stack when the precedences are equal.

The code that needs to change is as follows. Replace:

```cpp

while (!op.empty() && priority(op.top()) >= priority(cur_op)) 
```

with

```cpp

while (!op.empty() &&
       ((left_assoc(cur_op) && priority(op.top()) >= priority(cur_op)) ||
        (!left_assoc(cur_op) && priority(op.top()) > priority(cur_op))))

```

where left\_assoc is a function that decides whether an operator is left-associative.

Here is an implementation for the binary operators $+$, $-$, $*$, $/$ and the unary operators $+$ and $-$:

??? note "Sample code"
    ```cpp
    
    bool delim(char c) { return c == ' '; }
    
    bool is_op(char c) { return c == '+' || c == '-' || c == '*' || c == '/'; }
    
    bool is_unary(char c) { return c == '+' || c == '-'; }
    
    int priority(char op) {
      if (op < 0)  // unary operator
        return 3;
      if (op == '+' || op == '-') return 1;
      if (op == '*' || op == '/') return 2;
      return -1;
    }
    
    void process_op(stack<int>& st, char op) {
      if (op < 0) {
        int l = st.top();
        st.pop();
        switch (-op) {
          case '+':
            st.push(l);
            break;
          case '-':
            st.push(-l);
            break;
        }
      } else {  // pop the top elements, mind the order
        int r = st.top();
        st.pop();
        int l = st.top();
        st.pop();
        switch (op) {
          case '+':
            st.push(l + r);
            break;
          case '-':
            st.push(l - r);
            break;
          case '*':
            st.push(l * r);
            break;
          case '/':
            st.push(l / r);
            break;
        }
      }
    }
    
    int evaluate(string& s) {
      stack<int> st;
      stack<char> op;
      bool may_be_unary = true;
      for (int i = 0; i < (int)s.size(); i++) {
        if (delim(s[i])) continue;
    
        if (s[i] == '(') {
          op.push('(');  // 2. if a left parenthesis is encountered, put it onto the operator stack
          may_be_unary = true;
        } else if (s[i] == ')') {  // 3. if a right parenthesis is encountered, execute all operators inside the pair of parentheses
          while (op.top() != '(') {
            process_op(st, op.top());
            op.pop();  // keep outputting the top of the stack until a left parenthesis is encountered
          }
          op.pop();  // pop the left parenthesis
          may_be_unary = false;
        } else if (is_op(s[i])) {  // 4. if any other operator is encountered
          char cur_op = s[i];
          if (may_be_unary && is_unary(cur_op)) cur_op = -cur_op;
          while (!op.empty() &&
                 ((cur_op >= 0 && priority(op.top()) >= priority(cur_op)) ||
                  (cur_op < 0 && priority(op.top()) > priority(cur_op)))) {
            process_op(st, op.top());
            op.pop();  // keep outputting all operators with precedence greater than or equal to the current one
          }
          op.push(cur_op);  // push the new operator onto the operator stack
          may_be_unary = true;
        } else {  // 1. if a number is encountered, output it directly
          int number = 0;
          while (i < (int)s.size() && isalnum(s[i]))
            number = number * 10 + s[i++] - '0';
          --i;
          st.push(number);
          may_be_unary = false;
        }
      }
    
      while (!op.empty()) {
        process_op(st, op.top());
        op.pop();
      }
      return st.top();
    }
    
    ```

## References

**This page is mainly translated from the blog post [Разбор выражений. Обратная польская нотация](https://e-maxx.ru/algo/expressions_parsing) and its English translation [Expression parsing](https://cp-algorithms.com/string/expression_parsing.html). The Russian version is licensed under Public Domain + Leave a Link; the English version is licensed under CC-BY-SA 4.0.**

## Further reading

1.  [Operator-precedence\_parser](https://en.wikipedia.org/wiki/Operator-precedence_parser)
2.  [Shunting yard algorithm](https://en.wikipedia.org/wiki/Shunting_yard_algorithm)

## Exercises

1.  [NOIP2013 普及组 表达式求值 (NOIP 2013 Junior Division: Expression evaluation)](https://www.luogu.com.cn/problem/P1981)
2.  [后缀表达式 (Postfix expression)](https://www.luogu.com.cn/problem/P1449)
3.  [Transform the Expression](https://www.spoj.com/problems/ONP/)
