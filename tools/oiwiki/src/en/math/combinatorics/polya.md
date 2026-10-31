---
title: Pólya enumeration
---

Prerequisites: [Permutations](../permutation.md)

## Introduction

The Pólya enumeration theorem is usually used to solve counting problems that involve the notion of "essentially different" objects.

???+ info "This article may touch on group theory"
    This article may touch on content from group theory. It gives brief explanations of the group-theoretic concepts involved so that readers unfamiliar with that material can understand and apply the Pólya enumeration theorem. For the group-theoretic content, rigorous statements and discussion, see the chapters [Basic concepts of abstract algebra](../algebra/basic.md), [Group theory](../algebra/group-theory.md), etc.

??? info "“Symmetry group”, “symmetric group” and “permutation group”"
    This article will inevitably use the names of these three kinds of groups at the same time. Although they are easy to confuse, they really do refer to different concepts. Given a geometric structure, a symmetry operation on it is a geometric transformation that maps it onto itself, and the symmetry group is the set of these symmetry operations. The symmetric group is the set of all permutations of a given set. A permutation group is a subgroup of the symmetric group, i.e. a group formed by some (not necessarily all) permutations. Later we explain how to represent the symmetry group of a given geometric structure in the form of a permutation group and use it for counting problems.

## Burnside's lemma

Related reading: [Burnside's lemma](../algebra/group-theory.md#burnside-引理)

The Pólya enumeration theorem is an application and generalization of Burnside's lemma. Before introducing the Pólya enumeration theorem, we need to briefly review the content of Burnside's lemma.

To arrive at a general pattern, let us first consider a simple example.

???+ example "Coloring a necklace"
    We have a necklace with four beads in total, and each bead can be red or blue. Compute how many essentially different necklaces there are. (If two colorings can be made to coincide by rotating the necklace, they are considered the same.)

??? example "Solution and analysis"
    This problem is simple enough to be solved by enumeration. There are $4$ beads in total, and each bead can be colored in $2$ colors, so the total number of possible colorings of the necklace is $2^4=16$. Grouping together the colorings that can be obtained from one another by rotation gives $6$ groups in total, as shown in the figure below. (Here the code of a single coloring lists the colors clockwise starting from the bead in the lower left corner, $B$ stands for blue and $R$ for red; the codes of colorings in the same group have the same background color.)
    
    ![Coloring a necklace](../images/necklaces.svg)
    
    This example shows that, to compute the number of essentially different colorings, the key is really to know how many different colorings correspond to each essentially identical coloring. In other words, we need to determine the size of each group in the figure above.
    
    The colorings that can be put into the same group are exactly those colorings that can be transformed into one another by rotations. There are $4$ ways to rotate in total, namely
    
    $$
    G=\{r_0,r_1,r_2,r_3\},
    $$
    
    denoting rotation by $0,1,2,3$ steps respectively. Rotating by $0$ steps means staying in place.
    
    First look at the group containing the coloring $RRBB$. Applying these four operations to it gives, respectively,
    
    $$
    RRBB, RBBR, BBRR, BRRB.
    $$
    
    The four colorings are pairwise different, so this group has $4$ elements.
    
    Next look at the group containing the coloring $BRBR$. Applying the same four operations to it gives, respectively,
    
    $$
    BRBR, RBRB, BRBR, RBRB.
    $$
    
    Here the result of rotating twice coincides with the result of not rotating, and the result of rotating three times coincides with the result of rotating once. So this group has $2$ elements.
    
    Finally look at the groups containing the colorings $BBBB$ and $RRRR$. Applying the four operations to them always gives themselves. Hence each of these groups has only $1$ element.
    
    If we write $x$ for a coloring and $Gx$ for the set of color codes that can be obtained by applying the operations to the coloring $x$, then a pattern can be drawn from the example above: the effect of the operations of $G$ on $x$ has a certain "periodicity".
    
    Let $|G|$ denote the total number of operations. This "periodicity" of the effect means that if $m$ different operations of $G$ map the coloring $x$ to itself, then the results of applying these operations to $x$ repeat $m$ times each. Hence the coloring $x$ has $|G|/m$ different results under these operations in total, which is exactly the size of the group containing $x$.
    
    In this example, only the rotation by zero steps $r_0$ maps $RRBB$ to itself, so the size of its group equals $4/1=4$; both the rotation by zero steps $r_0$ and the rotation by two steps $r_2$ map $BRBR$ to itself, so the size of its group equals $4/2=2$; rotating by any number of steps maps $BBBB$ to itself, so the size of its group is $4/4=1$.
    
    In what follows, we write $G_x$ for the set of operations that map $x$ to itself, so $|G_x|$ is the $m$ above. Then the size of the group containing $x$ is $|G|/|G_x|$. To compute the number of groups of colorings, it suffices to go through all possible colorings $x\in X$ and assign to a coloring $x$ whose group has size $|Gx|$ the weight $1/|Gx|$; the number of groups can then be expressed as
    
    $$
    |X/G|=\sum_{x\in X}\frac{1}{|Gx|}=\sum_{x\in X}\frac{|G_x|}{|G|}.
    $$
    
    The form of this expression is not convenient to apply. Write $gx$ for the result of applying the operation $g\in G$ to the coloring $x\in X$; then the set $G_x$ described above is exactly $\{g\in G:gx=x\}$, so exchanging the order of summation gives
    
    $$
    \begin{aligned}
    \sum_{x\in X}|G_x| 
    &=\sum_{x\in X}|\{g\in G:gx=x\}|\\
    &=\sum_{x\in X}\sum_{g\in G}[gx=x]\\
    &=\sum_{g\in G}\sum_{x\in X}[gx=x]\\
    &=\sum_{g\in G}|\{x\in X:gx=x\}|\\
    &=\sum_{g\in G}|X^g|.
    \end{aligned}
    $$
    
    Here $[\cdot]$ is the Iverson bracket. In the result of exchanging the summation signs, $X^g=\{x\in X:gx=x\}$ denotes the set of colorings $x$ that stay unchanged under the operation $g$. In short, these are the fixed points of the operation $g$.
    
    After this discussion, the number of groups can now be written as
    
    $$
    |X/G|=\frac{1}{|G|}\sum_{g\in G}|X^g|.
    $$
    
    That is, the number of groups is the average number of fixed points of the rotations.
    
    As an application of this result, let us compute the number of necklace colorings once more. The fixed points of the rotations can be listed as follows.
    
    | Operation |        Fixed points       |
    | :---: | :-----------------------: |
    | $r_0$ |            $X$            |
    | $r_1$ |      $\{BBBB,RRRR\}$      |
    | $r_2$ | $\{BBBB,BRBR,RBRB,RRRR\}$ |
    | $r_3$ |      $\{BBBB,RRRR\}$      |
    
    Hence the number of groups equals
    
    $$
    \frac{16+2+4+2}{4} = 6.
    $$
    
    This recovers the earlier result.

From this example, a general result can be derived for solving this kind of counting problem. For convenience of discussion, this article considers the setting of coloring problems; of course, it can also be applied to other settings, and corresponding examples are given later.

A coloring problem says: given some structure, coloring each of its colorable objects (e.g. elements, vertices, edges, etc.) yields different colorings. The structure has some symmetry, which makes seemingly different colorings transform into one another after a sequence of symmetry operations. Colorings that can be transformed into one another are called essentially the same. The problem asks for the number of essentially different colorings.

According to the analysis in the example, to solve such a problem, one first has to discuss which symmetry operations the given structure has. The set $G$ of these symmetry operations is called the symmetry group of the given structure. In practical applications, most of the time there is no need to know the definition of a group; it suffices to be able to discuss all the symmetry operations without repetition or omission. Later in this article the structures of several common symmetry groups are analyzed, and the definition of a group is explained there.

The set of all colorings is denoted by $X$, and a single coloring in it by $x$. The result of the operation $g\in G$ acting on the coloring $x\in X$ is $gx$. Then the set of all results that can be obtained by some operation acting on the coloring $x$ is $Gx=\{gx:g\in G\}$, which is called the orbit of $x$ under the action of the group $G$. Different colorings in the same orbit are exactly what such problems call "essentially the same". Hence the number of all essentially different colorings is equivalent to the number of distinct orbits.

The analysis in the example can be generalized to the general case.

???+ note "Burnside's lemma"
    Given an action of a group $G$ on a set $X$, the number of all distinct orbits is
    
    $$
    |X/G|=\frac{1}{|G|}\sum_{g\in G}|X^g|.
    $$
    
    Here $X^g=\{x\in X:gx=x\}$ is the set of fixed points under the action of $g\in G$.

Its proof is almost a verbatim copy of the analysis in the example above. However, the example used an observation, namely that the result of the action of the group $G$ on a single element $x$ has a certain "periodicity", so that the number of repetitions of this period equals the number of operations mapping $x$ to itself. This observation is correct in the general case, but because the structure of the group $G$ may be very complicated, its "periodicity" is not necessarily as direct as it appears in the example. Stating this observation rigorously requires the [orbit-stabilizer theorem](../algebra/group-theory.md#稳定化子) from group theory.

In applications, as long as one can list all the symmetry operations and give the number of fixed points of each symmetry operation, the corresponding counting problem can be solved. Below is a slightly more complicated application.

???+ example "Coloring a cube"
    Color a cube with three colors. Find the number of essentially different colorings (two colorings that coincide after a rotation in space are regarded as the same).

??? example "Solution"
    Since the cube has $6$ faces and each face can be colored in $3$ ways, there are $3^6$ colorings in total, i.e. $|X|=3^6$. Denote the symmetry group of the cube by $G$.
    
    ![](../images/cube.svg)
    
    Next we need to analyze all the operations in $G$; they can be divided into the following classes (for convenience, we call the six faces of the cube front, back, top, bottom, left and right):
    
    -   Doing nothing, i.e. the identity transformation: since all colorings stay unchanged under the identity, it corresponds to $|X^g|=3^6$;
    -   Rotation by $90^\circ$ about the axis through the centers of two opposite faces: there are $3$ choices of the pair of opposite faces and $2$ choices of the direction of rotation, so this class contains $6$ permutations in total. Suppose the axis through the centers of the front and back faces is chosen; then the top, bottom, left and right faces must have the same color for the coloring to stay unchanged after the rotation. In this case there are $3$ regions that can be colored independently, so it corresponds to $|X^g|=3^3$;
    -   Rotation by $180^\circ$ about the axis through the centers of two opposite faces: there are $3$ choices of the pair of opposite faces, and the choice of the direction of rotation makes no difference, so this class contains $3$ permutations in total. Suppose the axis through the centers of the front and back faces is chosen; then the top and bottom faces must have the same color and the left and right faces must have the same color for the coloring to stay unchanged after the rotation. In this case there are $4$ regions that can be colored independently, so it corresponds to $|X^g|=3^4$;
    -   Rotation by $180^\circ$ about the axis through the midpoints of two opposite edges: there are $6$ choices of the pair of opposite edges, and the direction of rotation still makes no difference to the permutation, so this class contains $6$ permutations in total. Suppose the edge shared by the front and top faces and the edge shared by the bottom and back faces are chosen as the opposite edges; then the front and top faces must have the same color, the bottom and back faces must have the same color, and the left and right faces must have the same color for the coloring to stay unchanged after the rotation. In this case there are $3$ regions that can be colored independently, so it corresponds to $|X^g|=3^3$;
    -   Rotation by $120^\circ$ about the axis through two opposite vertices: there are $4$ choices of the pair of opposite vertices and $2$ choices of the direction of rotation, so this class contains $8$ permutations in total. Suppose the upper right corner of the front face and the lower left corner of the back face are chosen as the opposite vertices; then the front, top and right faces must have the same color and the back, bottom and left faces must have the same color for the coloring to stay unchanged after the rotation. In this case there are $2$ regions that can be colored independently, so it corresponds to $|X^g|=3^2$.
    
    Therefore the number of all essentially different colorings is
    
    $$
    \frac{1\times3^6+6\times3^3+3\times3^4+6\times3^3+8\times3^2}{1+6+3+6+8}=57.
    $$

## Pólya enumeration theorem

The statement of Burnside's lemma does not use the property that the set $X$ is the set of all colorings of some structure. In fact, the range of application of Burnside's lemma is not limited to coloring counting problems. For coloring counting problems, the Pólya enumeration theorem provides a more concrete method of computation. It can be regarded as the application of the general Burnside's lemma to coloring counting problems.

Compared with Burnside's lemma, the improvement of the Pólya enumeration theorem is that it provides a concrete method of computing the size $|X^g|$ of the fixed-point set in coloring counting problems.

This can be seen intuitively from the cube coloring example above. For each symmetry operation of the cube, the size of its fixed-point set has the form $m^{c(g)}$, where $m$ is the number of colors and $c(g)$ is the number of regions that can be colored independently under the operation $g$. This observation also holds in the general case, but it needs to be further clarified how to compute the value of $c(g)$ for a given $g$.

Choosing a coloring of some structure, expressed in mathematical language, is choosing a map $f:X\rightarrow C$ from the set $X$ of colorable objects of the structure (e.g. the beads of a necklace, the faces of a cube, etc.) to the set of colors $C$. Hence the set of colorings is $C^X$. The symmetry group $G$ of the structure acts on the structure, and so naturally also acts on the set $X$. Such a symmetry operation always corresponds to a bijection of the set $X$, i.e. a **permutation**.[^perm-group]

Now we analyze the structure of the fixed-point set $(C^X)^g$. Given $g$, regarded as a permutation of $X$, by analogy with the analysis in the example we know that if the position $x$ in $X$ can be moved to the position $y$ after finitely many repetitions of the operation $g$, then a fixed point $f\in (C^X)^g$ must satisfy $f(x)=f(y)$. In the language of orbits from the previous section, since the positions $x$ and $y$ lie in the same orbit of the action[^g-act] of the operation $g$, they need to be colored with the same color. In the language of permutations, in the [cycle decomposition](../permutation.md#cycle-notation) of the permutation $g$, the positions $x$ and $y$ lie in the same cycle, so they need to be colored with the same color. Different cycles in the cycle decomposition need not be colored the same and can be colored independently, so the number of regions that can be colored independently is $c(g)$, i.e. the number of cycles in the cycle decomposition of $g$.

Consequently, the number of fixed points of the operation $g$ is $|C|^{c(g)}$. Substituting this conclusion into Burnside's lemma yields the unweighted version of the **Pólya enumeration theorem**.

???+ note "Pólya enumeration theorem (unweighted version)"
    Given an action of a group $G$ on a set $X$ and a set of colors $C$, the number of distinct colorings is
    
    $$
    |C^X/G|=\frac{1}{|G|}\sum_{g\in G}m^{c(g)},
    $$
    
    where $m$ is the number of colors and $c(g)$ is the number of cycles in the cycle decomposition of the permutation representation of the element $g\in G$.

??? info "On the meaning of the group $G$"
    There is a slight abuse of notation here. If the group $G$ acts on $X$, the group action on the set of colorings $C^X$ needs to be redefined; we do not distinguish between them here.

As a simple application of the Pólya enumeration theorem, we now recompute the earlier examples using the Pólya enumeration theorem.

??? example "Alternative solution of the necklace coloring problem"
    Label the four beads $1\sim 4$; then the elements of the group $G$ in the example have the following permutation representations (all written in the form of cycle decompositions):
    
    -   rotation by zero steps $r_0=(1)$, $4$ cycles in total (note the omitted $1$‑cycles);
    -   rotation by one step $r_1=(1234)$, $1$ cycle in total;
    -   rotation by two steps $r_2=(13)(24)$, $2$ cycles in total;
    -   rotation by three steps $r_3=(1432)$, $1$ cycle in total.
    
    Therefore the number of essentially different colorings is
    
    $$
    \frac{2^4+2^1+2^2+2^1}{4}=6.
    $$

??? example "Alternative solution of the cube coloring problem"
    Since the earlier analysis has in fact already given the cycle representations of all classes of permutations, just without writing them out explicitly with numbers, we do not repeat the earlier analysis here. As an illustration, consider only the case of the rotation by $180^\circ$ about the axis through the midpoints of opposite edges. Number the front, back, top, bottom, left and right faces $1\sim6$ in this order; then the corresponding permutation is $(13)(24)(56)$, so $c(g)=3$. The other types of permutations can be analyzed similarly, and the final expression for the count is exactly the same as above.

## Generalization to the weighted form

The unweighted version of the Pólya enumeration theorem can only give the count of all essentially different colorings, but it is powerless when dealing with finer problems. For instance, if in the coloring problem above the number of available beads of each color is given, the Pólya enumeration formula above cannot be applied directly. When actually solving such problems, one needs to carry out the derivation with Burnside's lemma again; summarizing these results in the form of generating functions gives the weighted version of the Pólya enumeration theorem.

???+ example "Coloring a necklace (with restrictions)"
    We have a necklace with four beads in total, and each bead can be red or blue; exactly two red beads and two blue beads are available. Compute how many essentially different necklaces there are. (If two colorings can be made to coincide by rotating the necklace, they are considered the same.)

??? example "Solution and analysis"
    Let us use Burnside's lemma. There are two red beads and two blue beads, so there are $\dbinom{4}{2}=6$ colorings in total. The symmetry group $G=\{r_0,r_1,r_2,r_3\}$ corresponds to rotations by $0\sim3$ steps respectively, and their fixed-point sets are analyzed as follows:
    
    -   rotation by zero steps $r_0=(1)$: all $6$ colorings are fixed points;
    -   rotation by one step $r_1=(1234)$: a fixed point requires all beads to have the same color, so there are no fixed points;
    -   rotation by two steps $r_2=(13)(24)$: there are two regions that can be colored independently, both of size $2$, and they must be colored red and blue respectively, so the size of the fixed-point set is $2$;
    -   rotation by three steps $r_3=(1432)$: the same as the rotation by one step, there are no fixed points.
    
    So, by Burnside's lemma, the number of essentially different colorings is
    
    $$
    \frac{6+0+2+0}{4}=2.
    $$

From this example the following method of computation can be summarized. For problems restricting the number of each color, one again colors the cycles of each permutation in the symmetry group separately, but the number of times each color is used must be exactly equal to the given number. Such combinatorial problems usually have no explicit solution; apart from special cases that can be computed with [combinatorial methods](../combinatorics/combination.md), they often need to be solved as a [knapsack problem](../../dp/knapsack/basic.md).

The answer to such counting problems can be given via generating functions. Given a permutation $g$, if its [cycle type](../permutation.md#cycle-type-of-a-permutation) is $1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}$, i.e. it has $\alpha_k$ cycles of length $k$, and each cycle can be colored with one of $m$ colors, then in the generating function

$$
\prod_{k=1}^n\left(\sum_{i=1}^mx_i^k\right)^{\alpha_k}
$$

the coefficient of the monomial $x_1^{\beta_1}x_2^{\beta_2}\cdots x_m^{\beta_m}$ is exactly the number of colorings in which color $i$ is used $\beta_i$ times ($1\le i\le m$). The combinatorial meaning of the expression $\sum_{i=1}^mx_i^k$ in parentheses is: for a cycle of length $k$, the number of colorings using color $i$ $k$ times is $1$, and in all other cases the count is $0$; this exactly describes the requirement that all positions in the same cycle be colored identically.

Given the generating function for the number of colorings under the permutation $g$, applying Burnside's lemma to each monomial gives the number of essentially different colorings for each color combination. Since for each monomial the set of colorings counted by its coefficient is closed under the action of $G$, and taking the average is linear in the coefficients, the generating function for the number of essentially different colorings is

$$
\frac1{|G|}\sum_{g\in G}\prod_{k=1}^n\left(\sum_{i=1}^mx_i^k\right)^{\alpha_k}.
$$

Expanding this expression, the coefficient of each monomial gives the number of essentially different colorings for the given color combination.

In the above process, the generating function $\sum_{i=1}^mx_i^k$ for coloring each cycle is nothing special and can be replaced by other generating functions. Hence we have the following general version of the Pólya enumeration theorem.

???+ note "Cycle index of a permutation group"
    Given a permutation group $G$, the **cycle index** of the group $G$, usually denoted by $Z_G$ or $Z(G)$, is defined as
    
    $$
    Z_G(t_1,t_2,\cdots,t_n)=\frac{1}{|G|}\sum_{g\in G}t_1^{c_1(g)}t_2^{c_2(g)}\cdots t_n^{c_n(g)},
    $$
    
    where $c_k(g)$ is the number of cycles of length $k$ in the cycle decomposition of the permutation $g$, i.e. $1^{c_1(g)}2^{c_2(g)}\cdots n^{c_n(g)}$ is the cycle type of the permutation $g$.

???+ note "Pólya enumeration theorem (weighted version)"
    Given an action of a group $G$ on a set $X$, if the count of colorings of each point is given by the generating function $f(x_1,x_2,\cdots,x_m)$, then the generating function for the number of essentially different colorings of the set $X$ is
    
    $$
    Z_G(f(x_1^1,x_2^1,\cdots,x_m^1),f(x_1^2,x_2^2,\cdots,x_m^2),\cdots,f(x_1^n,x_2^n,\cdots,x_m^n)),
    $$
    
    where $Z_G(t_1,t_2,\cdots,t_n)$ is the cycle index of the group $G$.

Here, if the generating function for coloring a single position is $f(x_1,x_2,\cdots,x_m)$, then the generating function for coloring a cycle of length $k$ is $f(x_1^k,x_2^k,\cdots,x_m^k)$. This reflects the fact that if a coloring is a fixed point of the given permutation, all positions in the same cycle must be colored with the same color. Evaluating the generating function at $x_i=1$ gives the unweighted version of the Pólya enumeration theorem above.

The statement of the theorem uses the concept of the cycle index of a permutation group. It is independent of the concrete coloring problem. It describes the structure of the permutation group.

??? example "Alternative solution of the restricted necklace coloring problem"
    The cycle index of the rotation group is $\dfrac14\left(t_1^4+t_2^2+2t_4\right)$, and the generating function for coloring a single point is $r+b$, so the generating function for all colorings is
    
    $$
    \begin{aligned}
    F(r,b)&=\frac14\left((r+b)^4+(r^2+b^2)^2+2(r^4+b^4)\right)\\
    &=r^4+r^3b+2r^2b^2+rb^3+b^4.
    \end{aligned}
    $$
    
    The required count is the coefficient of $r^2b^2$, i.e. $2$ essentially different colorings in total. Incidentally, this expression also gives the counts under other restrictions.

### Applications

The weighted version of the Pólya enumeration theorem plays an important role in combinatorial counting problems. Here we briefly discuss its applications; a more general discussion can be found in [Symbolic method for combinatorial problems](../poly/symbolic-method.md#有限制的构造).

???+ example "Diamond necklace"
    We have a necklace with four identical beads in total, and several diamonds can be set on each bead. If there are four diamonds, how many essentially different ways are there to set them? (If two settings can be made to coincide by rotating the necklace, they are considered the same.)

??? example "Solution and analysis"
    The symmetry group of the necklace is still the same as before. Ignoring the restriction on the total number of diamonds, the generating function for the diamond settings of a single position is
    
    $$
    f(x)=1+x+x^2+\cdots=\sum_{i=0}^\infty x^i=\frac{1}{1-x}.
    $$
    
    Applying the weighted version of the Pólya enumeration theorem, the generating function for all diamond settings is
    
    $$
    \begin{aligned}
    F(x)&=\frac14\left(f(x)^4+f(x^2)^2+2f(x^4)\right)\\
    &=1+x+3x^2+5x^3+10x^4+\cdots.
    \end{aligned}
    $$
    
    Hence the required number of settings is the coefficient of $x^4$, i.e. $10$ settings in total. As a check, enumeration shows that they are
    
    $$
    4000,3100,3010,3001,2200,2020,2110,2101,2011,1111.
    $$
    
    Here each group of four digits gives the number of diamonds on each bead.

This example shows that the problems the weighted version of the Pólya enumeration theorem can solve are far broader than coloring counting problems. It provides a way of extending a count at a single point to a count of essentially different configurations of the whole structure. Coloring problems are just a special case of such problems.

## Common symmetry groups

One of the difficulties in problems related to Pólya enumeration lies in analyzing the structure of the permutation group. Here we briefly discuss the structure of common symmetry groups and describe them by their cycle indices. Note that for the symmetry group of the same structure, if the set of objects acted on is different, the corresponding [group action](../algebra/group-theory.md#群作用) is also different, and hence so are their permutation representations. For instance, the actions of the symmetry group of a cube on its vertices, edges and faces correspond respectively to the vertex permutation group, edge permutation group and face permutation group of the cube; the numbers of vertices, edges and faces are all different, so of course these permutation groups and the corresponding cycle indices are also all different. Therefore, when solving concrete problems, one must not neglect specifying the objects acted on by the group.

??? info "Relationship between symmetry groups and permutation groups"
    Although the two concepts are very similar, they are by no means the same object. In the language of group theory, given a symmetry group $G$ and its group action on a set $X$, the permutation representation of the group action actually provides a homomorphism $\varphi$ from the group $G$ to the symmetric group $S_X$, and in the context of combinatorial counting this permutation representation is usually faithful, i.e. $\ker\varphi=\{e\}$, so the homomorphism $\varphi$ is actually an embedding of the group $G$ into the group $S_X$. The permutation group in this article is the image of this embedding, i.e. $\varphi(G)$, which is isomorphic to the symmetry group $G$ itself. Therefore, for the symmetry group $G$ of the same structure, if the group actions are chosen differently, it is isomorphic to different permutation groups $\varphi(G)$ and thus has different cycle indices (isomorphic permutation groups do not necessarily have the same cycle index).

Given a structure, its symmetry group is the set of all operations that map it onto itself. It necessarily satisfies the following conditions:

-   applying two symmetry operations to the given structure in succession can be regarded as applying another symmetry operation, i.e. the set of symmetry operations is closed under composition;
-   the composition of symmetry operations is associative;
-   there is an identity symmetry operation, i.e. leaving the given structure unchanged is itself regarded as an operation;
-   every operation has an inverse operation that cancels the effect of the given operation.

A [group](../algebra/basic.md#群) is the abstraction of all concepts satisfying these conditions. The discussion of the structure of groups is the main subject of [group theory](../algebra/group-theory.md). The analysis here focuses mainly on symmetry groups, and the discussion of their structure mainly uses a geometric point of view. Common examples are given here, from which readers should pick up the usual ways of thinking for analyzing such problems.

### Cyclic group

Given a regular $n$-gon, the symmetry group formed by all of its rotations is called the cyclic group and is denoted by $C_n$. Writing $r$ for the counterclockwise rotation by $(360/n)^\circ$, the elements of the group $C_n$ can be written as

$$
C_n=\{e,r,r^2,\cdots,r^{n-1}\}.
$$

Here $r^k$ denotes the result of repeating the operation $r$ $k$ times, i.e. the counterclockwise rotation by $(360k/n)^\circ$, and $e=r^0$ denotes the identity transformation.

Whether we consider the action of the cyclic group on the set of all vertices or on the set of all edges of the regular $n$-gon, its permutation representation is the same. Let us analyze the permutation representation of the group action taking the set of all vertices as an example. Its cycle index is

$$
Z(C_n)=\frac1n\sum_{d\mid n}\varphi(d)t_{d}^{n/d}.
$$

Here $\varphi(\cdot)$ is [Euler's totient function](../number-theory/euler-totient.md) from number theory.

Counting only rotations, the symmetry group of a necklace of length $n$ is exactly $C_n$.

??? note "Analysis"
    Let the set of vertices be labeled $\{0,1,\cdots,n-1\}$ in counterclockwise order; then $r^k(i)=(i+k)\bmod n$. The set of vertices in the cycle containing vertex $i$ is
    
    $$
    \{(i+\ell k)\bmod n:\ell\in\mathbf Z\}.
    $$
    
    Clearly $i\equiv i+\ell k\pmod n$ if and only if
    
    $$
    \frac{n}{\gcd(k,n)}\mid\ell.
    $$
    
    This means that the length of the cycle containing any vertex $i$ is $\dfrac{n}{\gcd(k,n)}$. Therefore the permutation $r^k$ has $\gcd(k,n)$ cycles of equal length. Collecting like terms in the expression for the cycle index: given $d\mid n$, there are $\varphi(d)$ values of $k$ in total with $\gcd(k,n)=n/d$, and the monomials corresponding to them all have the form $t_d^{n/d}$, so the expression for the cycle index above is obtained.

### Dihedral group

Given a regular $n$-gon, all of its rotations and reflections about axes of symmetry also form a symmetry group; it is called the dihedral group and is denoted by $D_{2n}$. Writing $r$ for the counterclockwise rotation by $(360/n)^\circ$ and $s$ for the reflection about some given axis of symmetry (e.g. the line through the center and some vertex), the operations of the group $D_{2n}$ can be written as

$$
D_{2n}=\{e,r,\cdots,r^{n-1},s,sr,\cdots,sr^{n-1}\}.
$$

Here $r^k$ is still a rotation, while $sr^k$, although it means first rotating $k$ times and then reflecting about the given axis of symmetry, can equivalently be regarded as a reflection about another axis of symmetry. Therefore the group $D_{2n}$ contains $1$ identity transformation, $(n-1)$ rotations and $n$ reflections in total. Its group actions on the vertex set and on the edge set also have the same cycle index[^dihedral-edge], namely

$$
Z(D_{2n})=\frac12Z(C_n)+
\begin{cases}
\dfrac12t_1t_2^k,&n=2k+1,\\
\dfrac14\left(t_1^2t_2^{k-1}+t_2^k\right),&n=2k.
\end{cases}
$$

??? note "Analysis"
    The analysis of the set of rotations $r^k$ (including the identity transformation) in the group $D_{2n}$ is exactly the same as for the cyclic group $C_n$; the key is the analysis of the remaining reflections. Here we need to distinguish cases according to the parity of the number of vertices $n$.
    
    When $n=2k+1$, the axes of symmetry of all reflections join a vertex to the midpoint of the opposite edge; there are $n$ such axes of symmetry in total. After each reflection, the vertex on the axis of symmetry stays fixed while the other vertices are swapped in pairs, so there is $1$ fixed point ($1$‑cycle) and $k$ $2$‑cycles.
    
    When $n=2k$, there are two kinds of axes of symmetry. Half of the axes of symmetry join opposite vertices; reflecting about such an axis keeps the two vertices on the axis of symmetry fixed and swaps the remaining vertices in pairs, so there are $2$ fixed points ($1$‑cycles) and $(k-1)$ $2$‑cycles. The other half of the axes of symmetry join the midpoints of opposite edges; reflecting about such an axis swaps all vertices in pairs, so there are $k$ $2$‑cycles.
    
    Based on this analysis, the expression for the cycle index above can be written down.

### Symmetric group

Given $n$ elements, all permutations on them form a group, called the symmetric group of degree $n$ and denoted by $S_n$. It describes all the symmetries these $n$ elements can have. It is also the permutation representation of the action of these symmetry operations on the set of elements.

According to the analysis in the article [Permutations](../permutation.md#cycle-type-of-a-permutation), its cycle index is

$$
Z(S_n)=\sum_{\alpha_1+2\alpha_2+\cdots+n\alpha_n=n}\frac{t_1^{\alpha_1}t_2^{\alpha_2}\cdots t_n^{\alpha_n}}{1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}\alpha_1!\alpha_2!\cdots\alpha_n!}.
$$

Here we used the fact that the number of permutations of cycle type $1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}$ is

$$
\frac{n!}{1^{\alpha_1}2^{\alpha_2}\cdots n^{\alpha_n}\alpha_1!\alpha_2!\cdots\alpha_n!}.
$$

It satisfies the recurrence relation

$$
Z(S_n)=\frac1n\sum_{k=1}^nt_kZ(S_{n-k}),
$$

with the base case $Z(S_0)=1$. The combinatorial meaning of this recurrence relation is: to construct a permutation of $n$ elements, one can first choose the length $k$ of the cycle containing the point $n$, and then construct a permutation on the set of the remaining $(n-k)$ elements.

Given the complete graph on $n$ vertices, its symmetry group is exactly $S_n$. The cycle index of its action on the set of all vertices is given by $Z(S_n)$ above. However, the permutation representation of its action on the set of all edges is not the same. For instance, the sizes of the sets already differ: the number of all edges is $n(n-1)/2$. The case of edges requires additional analysis. A simple example is given here; the general case can be found in the exercises.

???+ example "Counting undirected simple graphs"
    Compute the number of undirected simple graphs on $4$ vertices up to isomorphism.

??? example "Solution"
    This amounts to coloring the edges of the complete graph on $4$ vertices with two colors and asking for the number of essentially different colorings. The symmetry group is $S_4$; we now analyze the cycle index of its edge permutation group $S_4^{(2)}$. Denote the four vertices by $a,b,c,d$ and number the six edges $1=ab$, $2=bc$, $3=cd$, $4=da$, $5=ac$, $6=bd$ in this order.
    
    -   The identity transformation ($1$ of them): the edges also stay fixed, so the corresponding monomial is $1\cdot t_1^6$;
    -   Swapping two vertices ($6$ of them): suppose $a$ and $b$ are swapped; then edges $1$ and $3$ stay fixed, while edges $2$ and $5$ are swapped and edges $4$ and $6$ are swapped, so the corresponding monomial is $6t_1^2t_2^2$;
    -   Cycling three vertices ($8$ of them): suppose the cycle is $(abc)$; then the edges $1,2,5$ between them are cycled accordingly, and the edges $4,6,3$ joining them to the fourth vertex $d$ are also cycled accordingly, so the corresponding monomial is $8t_3^2$;
    -   Swapping two pairs of vertices ($3$ of them): suppose vertices $a$ and $b$ are swapped and vertices $c$ and $d$ are swapped; then edges $1$ and $3$ stay fixed, while edges $2$ and $4$ are swapped and edges $5$ and $6$ are swapped, so the corresponding monomial is $3t_1^2t_2^2$;
    -   Cycling four vertices ($6$ of them): suppose the cycle is $(abcd)$; then the edges $1,2,3,4$ between adjacent vertices are cycled accordingly, and the edges $5,6$ between opposite vertices are swapped at the same time, so the corresponding monomial is $6t_2t_4$.
    
    Therefore the cycle index of the edge permutation group is
    
    $$
    Z(S_4^{(2)})=\frac{1}{24}(t_1^6+9t_1^2t_2^2+8t_3^2+6t_2t_4).
    $$
    
    By the Pólya enumeration theorem, the number of undirected simple graphs on $4$ vertices up to isomorphism is
    
    $$
    \frac{2^6+9\times 2^4+8\times 2^2+6\times 2^2}{24} = 11.
    $$

### Polyhedral groups

A polyhedral group is the symmetry group of a regular polyhedron. There are only five regular polyhedra: the regular tetrahedron, the cube, the regular octahedron, the regular dodecahedron and the regular icosahedron. Exchanging vertices and faces while preserving the adjacency relations among vertices, edges and faces yields the dual regular polyhedron. Among them, the regular tetrahedron is dual to itself, the cube is dual to the regular octahedron, and the regular dodecahedron is dual to the regular icosahedron. Using duality, the discussion of their symmetry groups can be simplified.

Counting only the rotations that can be performed in three-dimensional space, there are only three such symmetry groups.

-   The tetrahedral group, i.e. the symmetry group of the regular tetrahedron:

    -   the identity transformation;
    -   rotations by $120^\circ$ and $240^\circ$ about the axis through a vertex and the center of the opposite face;
    -   rotation by $180^\circ$ about the axis through the midpoints of opposite edges.

    In total $1+2\times4+1\times3=12$ symmetry operations.

    The cycle indices of the corresponding permutation groups are as follows.

    -   Vertex permutation group and face permutation group: $\dfrac1{12}\left(t_1^4+8t_1t_3+3t_2^2\right)$;
    -   edge permutation group: $\dfrac1{12}\left(t_1^6+8t_3^2+3t_1^2t_2^2\right)$.

-   The octahedral group, i.e. the symmetry group of the cube (and of the regular octahedron):

    -   the identity transformation;
    -   rotations by $120^\circ$ and $240^\circ$ about the axis through opposite vertices;
    -   rotation by $180^\circ$ about the axis through the midpoints of opposite edges;
    -   rotations by $90^\circ$, $180^\circ$ and $270^\circ$ about the axis through the centers of opposite faces.

    In total $1+2\times 4+1\times 6+3\times 3=24$ symmetry operations.

    The cycle indices of the corresponding permutation groups of the cube are as follows.

    -   Vertex permutation group: $\dfrac{1}{24}\left(t_1^8+8t_1^2t_3^2+9t_2^4+6t_4^2\right)$;
    -   edge permutation group: $\dfrac{1}{24}\left(t_1^{12}+8t_3^4+6t_1^2t_2^5+6t_4^3+3t_2^6\right)$;
    -   face permutation group: $\dfrac{1}{24}\left(t_1^6+8t_3^2+6t_2^3+6t_1^2t_4+3t_1^2t_2^2\right)$.

    The permutation groups of the regular octahedron are similar, except that the roles of vertices and faces are exchanged.

-   The icosahedral group, i.e. the symmetry group of the regular dodecahedron (and of the regular icosahedron):

    -   the identity transformation;
    -   rotations by $120^\circ$ and $240^\circ$ about the axis through opposite vertices;
    -   rotation by $180^\circ$ about the axis through the midpoints of opposite edges;
    -   rotations by $72^\circ$, $144^\circ$, $216^\circ$ and $288^\circ$ about the axis through the centers of opposite faces.

    In total $1+2\times 10+1\times 15+4\times 6=60$ symmetry operations.

    The cycle indices of the corresponding permutation groups of the regular dodecahedron are as follows.

    -   Vertex permutation group: $\dfrac{1}{60}\left(t_1^{20}+20t_1^2t_3^6+15t_2^{10}+24t_5^4\right)$;
    -   edge permutation group: $\dfrac{1}{60}\left(t_1^{30}+20t_3^{10}+15t_1^2t_2^{14}+24t_5^6\right)$;
    -   face permutation group: $\dfrac{1}{60}\left(t_1^{12}+20t_3^4+15t_2^6+24t_1^2t_5^2\right)$.

    The permutation groups of the regular icosahedron are similar, except that the roles of vertices and faces are exchanged.

The cycle indices given here are all for permutation groups acting on vertices, edges or faces separately. To color different kinds of objects at the same time, one needs to write down the joint cycle index.

## Exercises

### Coloring problems

These problems only require analyzing the structure of the permutation group and applying the Pólya enumeration theorem.

-   [Luogu P4980【模板】Polya 定理 (Template: Pólya's theorem)](https://www.luogu.com.cn/problem/P4980)
-   [Luogu P2561 \[AHOI2002\] 黑白瓷砖 (Black and white tiles)](https://www.luogu.com.cn/problem/P2561)
-   [TRANSP - Transposing is Fun](https://www.spoj.com/problems/TRANSP/)
-   [TRANSP2 - Transposing is Even More Fun](https://www.spoj.com/problems/TRANSP2/)
-   [Luogu P3307 \[SDOI2013\] 项链 (Necklace)](https://www.luogu.com.cn/problem/P3307)

When the available color combinations are restricted, the number of ways to color the cycles has to be found by knapsack DP or by combinatorial methods.

-   [Luogu P1446 \[HNOI2008\] Cards](https://www.luogu.com.cn/problem/P1446)
-   [UVA10601 Cubes](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1542)
-   [Luogu P4916 \[MtOI2018\] 魔力环 (Magic ring)](https://www.luogu.com.cn/problem/P4916)

### Graph enumeration

The Pólya enumeration theorem can be applied to [graph enumeration](../combinatorics/graph-enumeration.md) problems; the difficulty of such problems lies in enumerating the edge permutation group of the graph.

-   [SGU 282. Isomorphism](https://codeforces.com/problemsets/acmsguru/problem/99999/282)
-   [Luogu P4727 \[HNOI2009\] 图的同构计数 (Counting graph isomorphism classes)](https://www.luogu.com.cn/problem/P4727)
-   [Luogu P4128 \[SHOI2006\] 有色图 (Colored graphs)](https://www.luogu.com.cn/problem/P4128)

Another class of graph enumeration problems to which the Pólya enumeration theorem can be applied requires manipulating generating functions directly.

-   [LOJ 6538 烷基计数 加强版 加强版 (Counting alkyl groups, extra hard version)](https://loj.ac/p/6538)
-   [LOJ 6512「雅礼集训 2018」烷烃计数 (Counting alkanes)](https://loj.ac/p/6512)
-   [Luogu P6597 烯烃计数 (Counting alkenes)](https://www.luogu.com.cn/problem/P6597)
-   [Luogu P5818 \[JSOI2011\] 同分异构体计数 (Counting isomers)](https://www.luogu.com.cn/problem/P5818)

## References and notes

-   [Pólya enumeration theorem - Wikipedia](https://en.wikipedia.org/wiki/P%C3%B3lya_enumeration_theorem)
-   [Notes on Pólya's Enumeration Theorem](https://www.diva-portal.org/smash/get/diva2:324594/FULLTEXT01.pdf)
-   [Cycle index - Wikipedia](https://en.wikipedia.org/wiki/Cycle_index)

[^perm-group]: Therefore the symmetry group $G$ can be represented as a permutation group on the set $X$, i.e. a subgroup of the symmetric group $S_X$.

[^g-act]: Strictly speaking, it is the action of the subgroup $\langle g\rangle\le G$.

[^dihedral-edge]: Unlike the case of the cyclic group, when $n$ is even the permutation representations of these two group actions are not the same: a reflection about an axis of symmetry through opposite vertices has cycle type $1^22^{k-1}$ on the vertex set but $2^k$ on the edge set, while for a reflection about an axis of symmetry through the midpoints of opposite edges it is exactly the other way around. However, the numbers of axes of symmetry of these two kinds are equal, so the cycle index after summation is unchanged.
