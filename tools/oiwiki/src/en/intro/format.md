---
title: Style guide
---

Before this article begins, every member of the **OI Wiki** project team warmly welcomes you to contribute pages to this project. It is thanks to hundreds of people like you that **OI Wiki** has become what it is today!

This page lists the recommended formatting rules and editorial guidelines for writing **OI Wiki**. Before writing or correcting wiki pages, please read the following carefully to help you produce higher-quality content.

If you cannot wait to get started, read the [TL;DR](#tldr) and [Illustrated examples](#illustrated-examples) sections first.

??? abstract "Changelog"
    **Note**: only changes related to writing, reviewing, and similar activities are recorded, not formatting corrections.
    
    | Date | Main changes | Related issue/pull request links |
    | ---------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
    | 2026-02-22 | Refined the rules for quotation marks | [#6793](https://github.com/OI-wiki/OI-wiki/pull/6793)                                                       |
    | 2026-01-07 | Required the fullwidth full stop instead of the Chinese ideographic full stop | [#6746](https://github.com/OI-wiki/OI-wiki/pull/6746)                                                       |
    | 2025-08-10 | Added formatting requirements for the style guide itself;<br>code: expanded the requirements for code snippets | [#6412](https://github.com/OI-wiki/OI-wiki/pull/6412)                                                       |
    | 2025-08-10 | Added Changelog and TL;DR | [#6409](https://github.com/OI-wiki/OI-wiki/pull/6409)                                                       |
    | 2024-10-08 | Code: refined formatting requirements for cross-platform testing | [#5912](https://github.com/OI-wiki/OI-wiki/pull/5912), [#5924](https://github.com/OI-wiki/OI-wiki/pull/5924) |
    | 2024-03-26 | Use original OJ problem links rather than mirror links | [#5482](https://github.com/OI-wiki/OI-wiki/pull/5482)                                                       |
    | 2023-10-09 | Theme plugins: added formatting requirements for tabs[^note6] | [#5152](https://github.com/OI-wiki/OI-wiki/pull/5152)                                                       |
    | 2023-07-23 | Require references to official documentation for downloading and installing tools | [#5023](https://github.com/OI-wiki/OI-wiki/pull/5023)                                                       |
    | 2023-04-15 | Expanded the rules for quotation marks | [#4792](https://github.com/OI-wiki/OI-wiki/pull/4792)                                                       |
    | 2023-03-28 | LaTeX: mathematical symbols table | [#4587](https://github.com/OI-wiki/OI-wiki/pull/4587)                                                       |
    | 2023-03-02 | Expanded the rules for fullwidth and halfwidth punctuation, hyphens, and dashes | [#4726](https://github.com/OI-wiki/OI-wiki/pull/4726)                                                       |
    | 2022-12-13 | Theme plugins: removed the shadow-style requirement for nested collapsible blocks | [#4500](https://github.com/OI-wiki/OI-wiki/pull/4500)                                                       |
    | 2022-08-09 | Use Chinese headings when linking to sections of internal pages | [#4057](https://github.com/OI-wiki/OI-wiki/pull/4057)                                                       |
    | 2022-06-12 | Refined the requirements for navigation changes[^note4] | [#4043](https://github.com/OI-wiki/OI-wiki/pull/4043)                                                       |
    | 2021-09-09 | Theme plugins: expanded the requirements for collapsible blocks | [#3517](https://github.com/OI-wiki/OI-wiki/pull/3517)                                                       |
    | 2021-09-03 | LaTeX: `\Leftrightarrow` $\to$ `\iff` | [#3499](https://github.com/OI-wiki/OI-wiki/pull/3499)                                                       |
    | 2021-08-18 | Code: added formatting requirements for example-problem code | [#3447](https://github.com/OI-wiki/OI-wiki/pull/3447)                                                       |
    | 2021-08-12 | Images: prefer APNG for animations | [#3422](https://github.com/OI-wiki/OI-wiki/pull/3422)                                                       |
    | 2021-06-29 | Images: recommend submitting source files as well | [#3255](https://github.com/OI-wiki/OI-wiki/pull/3255)                                                       |
    | 2021-05-29 | Code: removed the same-line brace requirement and added readability requirements | [#3197](https://github.com/OI-wiki/OI-wiki/pull/3197)                                                       |
    | 2021-03-15 | Site maintenance: standardized how pull requests are merged[^note5] | [#3061](https://github.com/OI-wiki/OI-wiki/pull/3061)                                                       |
    | 2021-02-01 | LaTeX: `\lt` $\to$ `<`, `\gt` $\to$ `>` | [#2950](https://github.com/OI-wiki/OI-wiki/pull/2950)                                                       |
    | 2021-01-27 | Recommend backing up external links in the [Internet Archive](https://web.archive.org/) | [#2918](https://github.com/OI-wiki/OI-wiki/pull/2918)                                                       |
    | 2020-09-19 | Site maintenance: requirements for commit messages and pull request titles[^note4] | [#2744](https://github.com/OI-wiki/OI-wiki/pull/2744)                                                       |
    | 2020-10-18 | Images: prefer SVG | [#2215](https://github.com/OI-wiki/OI-wiki/pull/2215)                                                       |
    | 2020-08-05 | LaTeX: added formatting requirements for multiletter variables | [#2502](https://github.com/OI-wiki/OI-wiki/pull/2502)                                                       |
    | 2020-07-28 | LaTeX: prohibit more than two columns in the `cases` environment | [#2466](https://github.com/OI-wiki/OI-wiki/pull/2466)                                                       |
    | 2020-07-24 | LaTeX: `{n \choose m}`$\to$ `\dbinom{n}{m}` | [#2442](https://github.com/OI-wiki/OI-wiki/pull/2442)                                                       |
    | 2020-07-20 | Markdown: prohibit strikethrough syntax | [#2422](https://github.com/OI-wiki/OI-wiki/pull/2422)                                                       |
    | 2020-07-19 | Theme plugins: require indentation spaces on blank lines in collapsible blocks[^note3];<br>LaTeX: additional formatting requirements for mathematical formulas | [#2412](https://github.com/OI-wiki/OI-wiki/pull/2412)                                                       |
    | 2020-07-11 | Initial version | [#2350](https://github.com/OI-wiki/OI-wiki/pull/2350)                                                       |

## TL;DR

To help first-time readers, this section lists some key points from the guide:

-   File storage:

    -   Use lowercase file names with `-` instead of spaces. See [SAVE-1](#SAVE-1).

    -   Do not embed externally hosted images. See [SAVE-2](#SAVE-2).

    -   Use SVG images whenever possible, and only the SVG 1.1 standard. See [SAVE-3](#SAVE-3).

    -   Animations should use SVG or APNG. See [SAVE-4](#SAVE-4).

    -   If an image has a source file, submit it as well. See [SAVE-5](#SAVE-5).

    -   When adding an external link, include a snapshot link as well. See [SAVE-6](#SAVE-6).

    -   Do not write internal links as external links. See [SAVE-7](#SAVE-7).

-   Punctuation:

    -   Use punctuation correctly. End every sentence with a **period**. See [PUNC-1](#PUNC-1) through [PUNC-7](#PUNC-7).

    -   Distinguish hyphens, en dashes, and em dashes. See [PUNC-8](#PUNC-8).

-   Markdown and theme-extension syntax:

    -   Use only second-, third-, and fourth-level headings. Do not use headings instead of bold text. Do not write LaTeX formulas in headings. See [LINT-1](#LINT-1), [MDFM-1](#MDFM-1), [CONT-4](#CONT-4), [CONT-9](#CONT-9).

    -   Keep indentation consistent inside collapsible blocks[^note3] and tabs[^note6], **including blank lines**. **Do not omit** the indentation spaces on blank lines. See [LINT-6](#LINT-6), [MDFM-6](#MDFM-6).

    -   Do not use strikethrough syntax `~~foo~~`. See [LINT-3](#LINT-3).

    -   Write display formulas as

        ```text
        $$
        a^{2}=b^{2}+c^{2}
        $$
        ```

        instead of `$$a^{2}=b^{2}+c^{2}$$`. See [LINT-5](#LINT-5).

    -   Use collapsible blocks rather than blockquotes. See [MDFM-5](#MDFM-5).

    -   Use only ` ``` ` syntax for code blocks, and specify the language. See [LINT-7](#LINT-7), [MDFM-3](#MDFM-3).

-   LaTeX formulas:
    -   Do not conflict with the [mathematical symbols table](./symbol.md). See [MATH-1.1](#MATH-1.1).

    -   Pay attention to fonts. See [MATH-1.2](#MATH-1.2), [MATH-1.15](#MATH-1.15), [MATH-2.6](#MATH-2.6), [MATH-2.7](#MATH-2.7).

    -   Do not overuse LaTeX formulas. See [MATH-1.14](#MATH-1.14).

    -   Do not use programming-language notation in LaTeX formulas (such as $a==b$, $a<<1$, or $a\%b$). Do not chain square brackets ($a[i][j]$). See [MATH-1.9](#MATH-1.9), [MATH-1.10](#MATH-1.10).

-   Code:

    -   Keep code as simple and clear as possible, avoiding bad habits such as cramming code onto too few lines. Maximize readability and emphasize the algorithm's idea. See [CONT-10](#CONT-10).

    -   Inserting code directly into a Markdown document is not recommended. See [CODE-1.1](#CODE-1.1), [CODE-1.2](#CODE-1.2).

## Formatting requirements for this document

-   <span id="FREQ-1">FREQ-1</span>: when revising a rule in the style guide, update the Changelog as well. Formatting-only corrections do not require a Changelog entry.
-   <span id="FREQ-2">FREQ-2</span>: except in the [TL;DR](#tldr) section, each rule in the style guide must have a unique identifier matching the regular expression `(?<category>[A-Z]{4})-(?<id>[1-9][0-9]*(?:\.[1-9][0-9]*)*)`, where `category` should have an intuitive meaning. Explanatory text does not need an identifier.
-   <span id="FREQ-3">FREQ-3</span>: entries in [TL;DR](#tldr) must come from other sections of the style guide and end with references to the corresponding rule identifiers.
-   <span id="FREQ-4">FREQ-4</span>: once assigned, rule identifiers should not change. If a change is necessary (such as deleting or merging rules), add a notice such as "Deprecated" or "Moved to XXXX-id".

## Requirements for documentation contributions

When planning to contribute content, familiarize yourself as much as possible with these three areas:

-   Document storage format
-   Document coherence
-   Formatting requirements for remark-lint and $\rm{\LaTeX}$ formulas

### Document links and storage format

-   <span id="SAVE-1">SAVE-1</span>: **file names must be lowercase, with words separated by `-`.** For example: `file-name.md`.

-   <span id="SAVE-2">SAVE-2</span>: save all **externally hosted** images referenced in a document to the corresponding `images` folder **in this repository** (to avoid triggering some sites' hotlink protection). The recommended naming scheme is `MD document name + number` (see images in existing documents). For example, this document's file name is format, so its first image would be named `format1.png`.

-   <span id="SAVE-3">SAVE-3</span>: SVG images are recommended[^ref4] for sharper rendering and better scaling. Because **OI Wiki** components differ in their SVG support, images should follow the [SVG 1.1](http://www.w3.org/TR/SVG11/) standard.

-   <span id="SAVE-4">SAVE-4</span>: if you cannot or do not know how to create an SVG animation, use APNG[^apng]. Windows users can record with [ScreenToGif](https://www.screentogif.com), and Linux users with [Peek](https://github.com/phw/peek); select APNG recording in the settings. Otherwise, create a video such as MP4 first and convert it to APNG. With ffmpeg, use `ffmpeg -i filename.mp4 -f apng filename.apng -plays 0`.[^intro-apng]

-   <span id="SAVE-5">SAVE-5</span>: when an image has both a source file and an exported image (such as JPG and PSD, or SVG and TikZ TeX source), save the source file in the same directory with the same base name as the image.

-   <span id="SAVE-6">SAVE-6</span>: ensure that your document's reference links are stable. Linking to resources on **self-hosted** services (such as problems on a personal OJ) is **not recommended**. When adding an external link, also save it in the Internet Archive[^webarchive] in case an irreplaceable link becomes unavailable.

-   <span id="SAVE-7">SAVE-7</span>: omit the domain from internal links and use a relative path to the corresponding `.md` file. For example, on this page (`intro/format`), link to the miscellaneous introduction (`misc`) with `[Introduction to miscellaneous topics](../misc/index.md)`. Add a fragment to link to a particular section, such as [`[Pull request format](./htc.md#pull-request-format)`](./htc.md#pull-request-format). Get the fragment value from the button to the right of each heading or the links in the table of contents on the right of the page.

### Document coherence

**Coherence** means that the **content** must have the following properties:

-   <span id="STRC-1">STRC-1</span>: progress from simple to advanced; the difficulty should increase gradually.
-   <span id="STRC-2">STRC-2</span>: logical organization.

    -   <span id="STRC-2.1">STRC-2.1</span>: articles on algorithms or mathematical concepts should include the following whenever possible:

        1.  principle: explain the underlying principle;
        2.  examples: give 1 \~ 2 typical examples;
        3.  problems: under this heading, **give only the problem names and links**. For algorithmic problems, prefer OJs in this order: original OJ (foreign OJs must be readily accessible from China) > UOJ > LOJ > Luogu.

        Example page: [IDA\*](../search/idastar.md)

    -   <span id="STRC-2.2">STRC-2.2</span>: articles about tools should include the following whenever possible:

        1.  introduction: explain the tool's background and purpose.
        2.  setup: describe environment configuration and usage in detail. Refer to official documentation for downloading and installation whenever possible.

        Example page: [WSL (Windows 10)](../tools/wsl.md)

Unless the existing content is poor, contribute by **adding to it** rather than replacing it outright. If you are unsure, see [How to get in touch about the project](./about.md#how-to-get-in-touch) and contact the **OI Wiki** team.

### Basic document formatting requirements

#### Remark-lint formatting requirements

[remark-lint](https://github.com/remarkjs/remark-lint) can automatically standardize the style of project files. **OI Wiki**'s current configuration is hosted in [.remarkrc](https://github.com/OI-wiki/OI-wiki/blob/master/.remarkrc).

While configuring it, the **OI Wiki** team encountered some issues that remark-lint does not handle well. Please strictly follow these requirements when editing documents:

-   <span id="LINT-1">LINT-1</span>: do not use first-level headings such as `<h1>` or `# Heading`.

-   <span id="LINT-2">LINT-2</span>: put one halfwidth space after the heading marker, for example `## Introduction`.

-   <span id="LINT-3">LINT-3</span>: do not use strikethrough syntax, since remark-lint does not handle it well (another reason is that struck-out text is usually a joke that does little to help the reader understand and does not meet the [wording requirements](#CONT-5) under "Text content formatting requirements" below).

-   <span id="LINT-4">LINT-4</span>: lists:
    -   <span id="LINT-4.1">LINT-4.1</span>: put a blank line before a list to start a new paragraph.
    -   <span id="LINT-4.2">LINT-4.2</span>: in ordered lists (such as `1. Example`), put a space after the period.

-   <span id="LINT-5">LINT-5</span>: put a blank line before and after a display formula, or it will be treated as an inline formula.

-   <span id="LINT-6">LINT-6</span>: when using Details syntax beginning with `???` or `!!!`, every line belonging to the block must start with at least 4 spaces.

    **Even blank lines must retain the same indentation as the other lines. Do not use your editor's automatic trailing-whitespace trimming.**

    ???+ success "Example"
        In the following code, `␣` represents a space ` `.
        
        ```text
        ???+ warning
        ␣␣␣␣Remember to add 4 spaces before the text. The rest of the syntax is the same as Markdown.
        ␣␣␣␣
        ␣␣␣␣Without the 4 spaces, the text will not appear inside the Details block.
        ␣␣␣␣
        ␣␣␣␣What `???` means is explained [below](#MDFM-5).
        ```
        
        ???+ warning "Warning"
            Remember to add 4 spaces before the text. The rest of the syntax is the same as Markdown.
            
            Without the 4 spaces, the text will not appear inside the Details block.
            
            What `???` means is explained [below](#MDFM-5).

-   <span id="LINT-7">LINT-7</span>: use ` ```text` for code-styled plain-text blocks. Using only ` ``` ` without specifying a language can cause incorrect indentation.

#### Using punctuation

-   <span id="PUNC-1">PUNC-1</span>: end every sentence with a **period**.

<!-- scripts.linter.postprocess.fix_full_stop off -->

-   <span id="PUNC-2">PUNC-2</span>: use **fullwidth** and **halfwidth** punctuation correctly. Use fullwidth punctuation in Chinese and halfwidth punctuation in English. For English within Chinese text, see [Editorial rules for English in Chinese publications](https://www.nppa.gov.cn/xxgk/fdzdgknr/hybz/202210/t20221004_445147.html). In particular, use the fullwidth full stop "．" instead of the Chinese ideographic full stop "。".

<!-- scripts.linter.postprocess.fix_full_stop on -->

<!-- scripts.linter.postprocess.fix_quotation off -->

-   <span id="PUNC-3">PUNC-3</span>: because `“……”` and `‘……’` do not distinguish fullwidth from halfwidth, use `「……」` for fullwidth double quotation marks, `"..."` for halfwidth double quotation marks, `『……』` for fullwidth single quotation marks, and `'...'` for halfwidth single quotation marks.

<!-- scripts.linter.postprocess.fix_quotation on -->

-   <span id="PUNC-4">PUNC-4</span>: distinguish the **Chinese enumeration comma** from the **regular comma**.
-   <span id="PUNC-5">PUNC-5</span>: pay attention to **parenthesis** placement. Parentheses within a sentence and those enclosing a whole sentence are placed differently.
-   <span id="PUNC-6">PUNC-6</span>: generally use **semicolons** to show the relationship between compound sentences in a list.
-   <span id="PUNC-7">PUNC-7</span>: in ordered lists, end each item with a **semicolon** and the last item with a **period**; in unordered lists, end each item with a **period**.
-   <span id="PUNC-8">PUNC-8</span>: distinguish the hyphen (usually replaced by U+002D hyphen-minus (-), the "minus" on the keyboard), U+2013 en dash (–), and U+2014 em dash (—). (When joining multiple people's names in English, use an en dash, although a hyphen is very often used incorrectly. Other mistakes are rarer, so this is the main point to remember.) See [Dash - Wikipedia](https://en.wikipedia.org/wiki/Dash).

    ???+ success "Example"
        -   中学生学科竞赛主要包括信息学奥林匹克竞赛、信息学奥林匹克竞赛、信息学奥林匹克竞赛、信息学奥林匹克竞赛和信息学奥林匹克竞赛（谁写的这个示例，建议抬走）． (Secondary-school subject competitions mainly include the Informatics Olympiad, the Informatics Olympiad, the Informatics Olympiad, the Informatics Olympiad, and the Informatics Olympiad (whoever wrote this example should be carried away).)
        -   「你吃了吗？」李四问张三． ("Have you eaten?" Li Si asked Zhang San.)
        -   我想对你说：「我真是太喜欢你了．」 (I want to tell you: "I really like you so much.")
        -   「苟利国家生死以，岂因祸福避趋之！」 ("If it benefits the country, I will risk my life; why should I avoid or pursue it according to personal fortune or misfortune!")
        -   张华考上了大学；李萍进了技校；我当了工人：我们都有美好的前途．[^note1] (Zhang Hua got into college; Li Ping entered a vocational school; I became a worker: we all have bright futures.)
        -   以下是这个算法的基本流程： (The algorithm's basic procedure is:)
            1.  初始化到各点的距离为无穷大，将所有点设置为未被访问过，初始化一个队列； (initialize distances to all vertices to infinity, mark all vertices as unvisited, and initialize a queue;)
            2.  将起点放入队列，将起点设置为已被访问过，更新到起点的距离为 $0$； (enqueue the starting vertex, mark it as visited, and set its distance to 0;)
            3.  取出队首元素，将该元素设置为未被访问过； (dequeue the front element and mark it as unvisited;)
            4.  遍历所有与此元素相连的边，若到这个点存在更短的距离，则进行松弛操作； (traverse all edges connected to this element and perform relaxation if a shorter distance to a vertex exists;)
            5.  若这个点未被访问过，则将这个点放入队列，且设置这个点为已经访问过； (if that vertex is unvisited, enqueue it and mark it as visited;)
            6.  回到第三步，直到队列为空． (return to step three until the queue is empty.)
        -   KMP 算法（Knuth–Morris–Pratt algorithm, KMP algorithm）由 Knuth、Pratt 和 Morris 在 1977 年共同发布．[^note2] (The KMP algorithm (Knuth–Morris–Pratt algorithm, KMP algorithm) was jointly published by Knuth, Pratt, and Morris in 1977.)

#### Markdown and theme-extension formatting requirements

-   <span id="MDFM-1">MDFM-1</span>: use `**SOMETHING**` and quotation marks for emphasis, not headings, since headings can disrupt the article's hierarchy and/or table of contents.

-   <span id="MDFM-2">MDFM-2</span>: when linking to a problem, use the original OJ's problem link rather than a mirror whenever possible.

-   <span id="MDFM-3">MDFM-3</span>: use Markdown's block features correctly. Enclose inline code in a pair of backticks, and code blocks in a pair of ` ``` ` fences. The backtick is the symbol below the tilde at the upper left of the keyboard. For code blocks, add the language name after the first ` ``` ` (for example, ` ```cpp`).

    ???+ success "Example"
        ````text
        ```cpp
        // #include<stdio.h>    //Bad style
        #include <cstdio>  //Good style
        ```
        ````
        
        ```cpp
        // #include<stdio.h>    //Bad style
        #include <cstdio>  //Good style
        ```

-   <span id="MDFM-4">MDFM-4</span>: write "References and notes" using Markdown footnotes. The format is:

    ```markdown
    Text.[^footnote-name]
    [^footnote-name]: Reference content. Note: use a halfwidth colon followed by a space.
    ```

    Footnote names may be numbers or text. Place footnote markers according to the same rules as parentheses. For a consistent appearance, use a uniform naming scheme within a page, such as ref1, ref2, note1…

    Place all footnote content under the second-level heading `## References and notes`.

    ???+ success "Example"
        ```markdown
        When `#include <cxxxx>` can replace `#include <xxxx.h>`, use the former.[^ref1]
        
        On January 21, 2020, CCF announced the resumption of NOIP.[^ref2]
        
        ## References and notes
        
        [^ref1]: [cstdio stdio.h namespace](https://stackoverflow.com/questions/10460250/cstdio-stdio-h-namespace)
        
        [^ref2]: [CCF announcement on resuming NOIP - China Computer Federation](https://www.ccf.org.cn/c/2020-01-21/694716.shtml)
        ```
        
        When `#include <cxxxx>` can replace `#include <xxxx.h>`, use the former.[^ref1]
        
        On January 21, 2020, CCF announced the resumption of NOIP.[^ref2]

-   <span id="MDFM-5">MDFM-5</span>: use the theme extension's `???+note` format (that is, [Collapsible Blocks](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#collapsible-blocks)) for problem statements and reference code. You can also use it for other supplementary content.

    Example code (`␣` below represents a space ` `):

    ```text
    ??? note "Title"
    ␣␣␣␣This block is collapsed by default.
    ␣␣␣␣
    ␣␣␣␣Place **solution code** inside a collapsible block.

    ???+note "[HDOJ's 'A + B Problem'](https://acm.hdu.edu.cn/showproblem.php?pid=1000)"
    ␣␣␣␣Titles can also contain Markdown links. This link points to HDOJ's "A + B Problem".
    ␣␣␣␣
    ␣␣␣␣This is also the recommended way to **link to the original problem**.
    ␣␣␣␣
    ␣␣␣␣Pay attention to the placement of double quotation marks.
    ```

    Result:

    ??? note "Title"
        This block is collapsed by default.
        
        Place **solution code** inside a collapsible block.

    ???+ note "[HDOJ's 'A + B Problem'](https://acm.hdu.edu.cn/showproblem.php?pid=1000)"
        Titles can also contain Markdown links. This link points to HDOJ's "A + B Problem".
        
        This is also the recommended way to **link to the original problem**.
        
        Pay attention to the placement of double quotation marks.

    The difference is that a block with `+` is expanded by default, while one without `+` is collapsed by default.

    Enclose the collapsible block's title, the content after `note` in `???+note`, in `"`. The title supports Markdown syntax. See [Admonition - Changing the title](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#changing-the-title). (Blocks without collapsing are regular admonitions; see [Admonitions - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions).)

-   <span id="MDFM-6">MDFM-6</span>: when adding code in different languages, use Content tabs to switch between languages. Tabs have other uses too; see [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage). Their usage and appearance are shown below.

    ???+ success "Example"
        Add 4 spaces before the text (represented by `␣` below). The rest of the syntax is the same as Markdown.
        
        ````text
        === "C"
        ␣␣␣␣```c
        ␣␣␣␣#include <stdio.h>
        ␣␣␣␣
        ␣␣␣␣int main(void) {
        ␣␣␣␣  printf("Hello world!\n");
        ␣␣␣␣  return 0;
        ␣␣␣␣}
        ␣␣␣␣```
        
        === "C++"
        ␣␣␣␣```cpp
        ␣␣␣␣#include <iostream>
        ␣␣␣␣
        ␣␣␣␣int main(void) {
        ␣␣␣␣  std::cout << "Hello world!" << std::endl;
        ␣␣␣␣  return 0;
        ␣␣␣␣}
        ␣␣␣␣```
        ````
        
        === "C"
            ```c
            #include <stdio.h>
            
            int main(void) {
              printf("Hello world!\n");
              return 0;
            }
            ```
        
        === "C++"
            ```cpp
            #include <iostream>
            
            int main(void) {
              std::cout << "Hello world!" << std::endl;
              return 0;
            }
            ```

If you have more questions about mkdocs-material (the theme we use), see the [MkDocs usage guide](https://github.com/ctf-wiki/ctf-wiki/wiki/Mkdocs-%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E), which explains how to use the theme's plugins.

#### Text content formatting requirements

-   <span id="CONT-1">CONT-1</span>: every occurrence of **OI Wiki** should be bold.

-   <span id="CONT-2">CONT-2</span>: start the page with a short overview of its content (such as "This page introduces…").

    ???+ success "Example"
        This page lists the recommended formatting rules and editorial guidelines for writing **OI Wiki**.

-   <span id="CONT-3">CONT-3</span>: if a page requires prior knowledge, add a line **Prerequisites: …** at the beginning, before the overview. The format is:

    `Prerequisites: [Internal page 1](url1), [Internal page 2](url2), and [Internal page 3](url3)`

    ???+ success "Example"
        Prerequisites: [Time complexity](../basic/complexity.md)
        
        This page introduces the basics of computation theory.

-   <span id="CONT-4">CONT-4</span>: pay attention to document structure. It should be well organized with a clear hierarchy. Please do not let "fifth-level headings" happen again; an ordinary article does not need such a complex hierarchy.

-   <span id="CONT-5">CONT-5</span>: pay attention to wording. As an encyclopedia, **OI Wiki** should use formal, objective language. Jokes and other content that does little to help readers understand should not appear on **OI Wiki**.

-   <span id="CONT-6">CONT-6</span>: give links complete titles or recognizable descriptions. Avoid bare URLs and vague wording such as "this" or "here". Describe each link as clearly as possible so readers know where it leads.

    The source article's or browser tab's title is recommended.

    ???+ failure "Not recommended"
        ```markdown
        See [this page](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
        
        See <https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork>
        ```
        
        See [this page](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
        
        See <https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork>

    ???+ success "Recommended"
        ```markdown
        See GitHub's official help page [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)
        ```
        
        See GitHub's official help page [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

-   <span id="CONT-7">CONT-7</span>: because of Markdown limitations, the second-level heading `## References and notes` must be at the end of the document.

-   <span id="CONT-8">CONT-8</span>: write ordinal numbers in Chinese words. Examples:
    -   The first term of a sequence.
    -   The first line of the input file.

-   <span id="CONT-9">CONT-9</span>: avoid MathJax formulas in headings of any level, as they may cause the table of contents to display incorrectly.[^ref3]

-   <span id="CONT-10">CONT-10</span>: pay attention to code readability.

    -   <span id="CONT-10.1.1">CONT-10.1.1</span>: code should have clear logic and be as simple and understandable as possible. Do not cram too much onto one line or introduce excessive unrelated code. Avoid content unrelated to the algorithm's idea.
    -   <span id="CONT-10.1.2">CONT-10.1.2</span>: add appropriate comments to reference code to help readers understand it.

    For languages such as C/C++:

    -   <span id="CONT-10.2.1">CONT-10.2.1</span>: avoid preprocessor directives and macro definitions that hinder readability.

    -   <span id="CONT-10.2.2">CONT-10.2.2</span>: do not use `0` instead of `false`/`NULL`/`nullptr`, or `1` instead of `true`, and so on.

    -   <span id="CONT-10.2.3">CONT-10.2.3</span>: when declaring [type aliases](https://en.cppreference.com/w/cpp/language/type_alias), prefer `using` over `typedef`.

    -   <span id="CONT-10.2.4">CONT-10.2.4</span>: do not define constants with macros; use keywords such as `constexpr`/`const` directly.

    -   <span id="CONT-10.2.5">CONT-10.2.5</span>: the `inline` keyword is not recommended for functions; see [Compiler optimizations](../lang/optimizations.md#inline---内联).

    -   <span id="CONT-10.2.6">CONT-10.2.6</span>: avoid complex template metaprogramming techniques such as type traits and partial specialization. If they are necessary, add comments explaining them.

        ???+ failure "Not recommended"
            ```cpp
            --8<-- "docs/intro/code/format/format_1.cpp:not-recommended"
            ```
            
            This code gives a complex implementation of the [greatest common divisor](../math/number-theory/gcd.md), where:
            
            -   The first `gcd` accepts two unsigned integers `x`, `y` and returns their greatest common divisor; the return type's range is guaranteed to include both `x` and `y`.
            -   The second `gcd` accepts two integers `x`, `y`, at least one of which is signed, and returns their greatest common divisor.
            -   The third `gcd` accepts more than two integers and returns their greatest common divisor.
            -   The fourth `gcd` accepts a container and returns the greatest common divisor of all its numbers.
            
            For **OI Wiki**, we care only about the idea behind the greatest-common-divisor algorithm. This code contains too many unrelated, complex technical details and should be avoided.

        ???+ success "Recommended"
            ```cpp
            --8<-- "docs/intro/code/format/format_1.cpp:recommended"
            ```
            
            "Adding type checks," "handling negative input," and "supporting multiple arguments" are more engineering concerns; our focus should always be the algorithm's idea.

#### LaTeX formula formatting requirements

LaTeX is the preferred choice for typesetting formulas, and we should use it correctly. We therefore have strict requirements for its use. For a quick start, read the table at the end of this section.

-   <span id="MATH-1.1">MATH-1.1</span>: your symbols must not conflict with those specified in the [mathematical symbols table](./symbol.md).

-   <span id="MATH-1.2">MATH-1.2</span>: use Roman type for numbers, constants, operators, and functions, and Italic type for variables and subscripts. LaTeX predefines some common constants, functions, operators, and so on, which we can call directly, including but not limited to:

    ```latex
    \log, \ln, \lg, \sin, \cos, \tan, \sec, \csc, \cot, \gcd, \min, \max, \exp, \inf, \mod, \bmod, \pmod
    ```

    When entering constants, function names, operators, and similar items, first check whether Roman type or another font is needed. For LaTeX symbols, see [KaTeX's Supported Functions page](https://katex.org/docs/supported.html) (not exhaustive), or search for an answer.

    Because lowercase Greek letters in Roman type are difficult to produce in LaTeX, lowercase Greek constants, operators, and functions may use Italic type, such as $\pi$ and the expression $\delta x$ with $\delta$.

    For a **function name** that is not predefined but needs Roman type, use `$\operatorname{something}$`; for example, `$\operatorname{lcm}$` produces an upright least-common-multiple (function) symbol. Similarly, use `$\mathrm{}$` for Roman **constants**, `$\mathbf{}$` for bold Roman symbols, and `$\boldsymbol{}$` for bold Italic symbols (such as the vector $\boldsymbol{a}$). Use `$\textit{}$` for multiletter variables. Use `$\text{}$` for all other nonmathematical content, including English text and special symbols. We recommend keeping Chinese text out of LaTeX formulas.

-   <span id="MATH-1.3">MATH-1.3</span>: if an expression needs line breaks (often in long display formulas), follow these rules:

    -   <span id="MATH-1.3.1">MATH-1.3.1</span>: put line breaks before $=$, $+$, $-$, $\pm$, $\mp$, and, if necessary, before $\times$, $\cdot$, $/$, for example:

        $$
        \begin{aligned}
            \mathrm{e}^x &= \sum\limits_{n=0}^{\infty} \frac{x^n}{n!} \\
            &= \phantom{+} 1 + x + \frac{x^2}{2} \\
            & \phantom{=} + \frac{x^3}{6} + \frac{x^4}{24} + \dots \\
        \end{aligned}
        $$

    -   <span id="MATH-1.3.2">MATH-1.3.2</span>: the same operator should not appear on both sides of a line break,

    -   <span id="MATH-1.3.3">MATH-1.3.3</span>: avoid line breaks inside parenthesized expressions.

-   <span id="MATH-1.4">MATH-1.4</span>: use `$\dfrac{}{}$` for inline fractions. For example, `$\dfrac{1}{2}$` renders as $\dfrac{1}{2}$, rather than `$\frac{1}{2}$`, which renders as $\frac{1}{2}$.

-   <span id="MATH-1.5">MATH-1.5</span>: use `\dbinom{n}{m}` for binomial coefficients, rendering as $\dbinom{n}{m}$, not `{n \choose m}` (no longer recommended in LaTeX). As with the previous rule for fractions, do not use `\binom{n}{m}`, rendering as $\binom{n}{m}$.

-   <span id="MATH-1.6">MATH-1.6</span>: avoid large operators in inline formulas (such as $\sum$, $\prod$, $\int$).

-   <span id="MATH-1.7">MATH-1.7</span>: when unambiguous, use `$\times$` instead of an asterisk; use `$\times$` for cross products and `$\cdot$` for dot products. For example, $a\times b$, $a\cdot b$, not $a\ast b$.

-   <span id="MATH-1.8">MATH-1.8</span>: use `$\cdots$` (midway between the baseline and top line), `$\ldots$` (on the baseline), or `$\vdots$` (vertical dots) instead of `$...$`. For example, $a_1,a_2,\cdots a_n$, not $a_1,a_2,... a_n$.

-   <span id="MATH-1.9">MATH-1.9</span>: outside code, use LaTeX formulas rather than programming-language notation. For example, use `$=$` rather than `$==$` ($a=b$, not $a==b$); `` `a<<1` `` or `$a\times 2$` rather than `$a<<1$`; and `$a\bmod b$` rather than `$a\%b$` ($a\bmod b$, not $a\%b$).

-   <span id="MATH-1.10">MATH-1.10</span>: in formulas, use subscripts rather than chained square brackets (C++ multidimensional-array notation): $a_{i,j,k}$, not $a[i][j][k]$. For complicated subscripts, use a multivariate function ($f(i,j,k)$) or inline code. For simple univariate functions, `$f_i$`, `$f(i)$`, and `$f[i]$` are all acceptable.

-   <span id="MATH-1.11">MATH-1.11</span>: for consistency and ease of writing, use `$O()$` rather than `$\mathcal O()$` for big $O$ in complexity analysis.

-   <span id="MATH-1.12">MATH-1.12</span>: for equivalence, use `$\iff$`, rendering as $\iff$, rather than `$\Leftrightarrow$`, rendering as $\Leftrightarrow$.

-   <span id="MATH-1.13">MATH-1.13</span>: the `cases` environment for piecewise functions **must have only two columns** (one `&` separator).

-   <span id="MATH-1.14">MATH-1.14</span>: do not overuse LaTeX formulas. This slows page loading (MathJax is famously inefficient) and can disrupt the layout. We normally use LaTeX math fonts for variable names. Avoid unnecessary **heavy** mixing of formulas and regular text, and avoid formulas when they are not needed. For example:

    ```LaTeX
    我们将要学习 $Network-flow$ 中的 $SPFA$ 最小费用流，需要使用 $Edmonds–Karp$ 算法进行增广．
    ```

    This is a typical example of **misusing math fonts**. (Use `*text*` for italics on a page.) (We will study SPFA minimum-cost flow in Network-flow, using the Edmonds–Karp algorithm for augmentation.)

-   <span id="MATH-1.15">MATH-1.15</span>: use the appropriate LaTeX symbols, especially Greek letters and other special symbols in formulas. For example, use `$\varphi$` for Euler's totient function, `$\Phi$` for a circle's diameter, and `$\phi$` for the golden ratio. Although they all represent the Greek letter phi, they have different meanings in different contexts. **Do not insert them using your input method's special-symbol feature.**

    For historical reasons in LaTeX, use `$\varnothing$` rather than `$\emptyset$` for the empty set; write other symbols according to the [mathematical symbols table](./symbol.md).

The table below summarizes the above. It does not cover every symbol, only common mistakes. Apply the same principles to similar situations.

| Noncompliant usage | Rendering | Compliant usage | Rendering |
| ---------------------------- | ----------------- | ---------------------------------------- | ----------------------------------- |
| `$log, ln, lg$`              | $log, ln, lg$     | `$\log$, $\ln$, $\lg$`                   | $\log$, $\ln$, $\lg$                  |
| `$sin, cos, tan$`            | $sin, cos, tan$   | `$\sin$, $\cos$, $\tan$`                 | $\sin$, $\cos$, $\tan$                |
| `$gcd, lcm$`                 | $gcd, lcm$        | `$\gcd$, $\operatorname{lcm}$`           | $\gcd$, $\operatorname{lcm}$         |
| `$e$, $\text{e}$, e` (base of the natural logarithm) | $e$, $\text{e}$, e | `$\mathrm{e}$` | $\mathrm{e}$ |
| `$i$, $\text{i}$, i` (imaginary unit) | $i$, $\text{i}$, i | `$\mathrm{i}$` | $\mathrm{i}$ |
| `$ 小于 a 的质数 $`               | $小于 a 的质数$        | `小于 $a$ 的质数`                             | 小于 $a$ 的质数 (primes less than a) |
| `$...$`                      | $...$             | `$\cdots$, $\ldots$, $\vdots$, $\ddots$` | $\cdots$, $\ldots$, $\vdots$, $\ddots$ |
| `$a*b$` (multiplying two numbers) | $a*b$ | `$a\times b$, $a\cdot b$` | $a\times b$, $a\cdot b$ |
| `$SPFA$` (English name) | $SPFA$ | `SPFA` | SPFA |
| `$a==b$`                     | $a==b$            | `$a=b$`                                  | $a=b$                               |
| `$f[i][j][k]$`               | $f[i][j][k]$      | `$f_{i,j,k}$, $f(i,j,k)$`                | $f_{i,j,k}$, $f(i,j,k)$              |
| `$R,N^*$` (sets) | $R,N^*$ | `$\mathbf{R}$, $\mathbf{N}^*$` | $\mathbf{R}$, $\mathbf{N}^*$ |
| `$\emptyset$`                | $\emptyset$       | `$\varnothing$`                          | $\varnothing$                       |
| `$size$`                     | $size$            | `$\textit{size}$`                        | $\textit{size}$                     |

#### Additional formatting requirements for mathematical formulas

Although the formula syntax above is very similar to the actual LaTeX typesetting system, **MathJax and LaTeX are two completely unrelated systems**. MathJax merely uses some syntax very similar to LaTeX. Many details differ, often making formulas incompatible between them.

Because **OI Wiki** developed a PDF export tool using the LaTeX typesetting engine, compatibility between MathJax and LaTeX matters. **Pay attention to the following when writing mathematical formulas on the wiki.**

These rules already accommodate MathJax as much as possible. The export tool supports some notation that originally rendered correctly only in MathJax.

-   <span id="MATH-2.1">MATH-2.1</span>: use `\begin{aligned} ... \end{aligned}` for multiline aligned formulas;

-   <span id="MATH-2.2">MATH-2.2</span>: if these multiline aligned formulas need **numbering**, use `align` or `equation`;

-   <span id="MATH-2.3">MATH-2.3</span>: do not use the `split` or `eqnarray` environments;

-   <span id="MATH-2.4">MATH-2.4</span>: do not use `\lt`, `\gt` for less-than and greater-than signs; use `<`, `>` directly;

-   <span id="MATH-2.5">MATH-2.5</span>: do not use `\\` directly for line breaks (put formulas needing line breaks inside `aligned` or another multiline environment);

-   <span id="MATH-2.6">MATH-2.6</span>: to produce the LaTeX logo $\rm{\LaTeX}$, use `$\rm{\LaTeX}$`, not `mathrm`; (`\LaTeX` cannot be used in math mode in TeX, while `\mathrm` cannot be used in normal mode; although `\text` works correctly in TeX, MathJax outputs its argument literally rather than interpreting commands);

-   <span id="MATH-2.7">MATH-2.7</span>: Chinese text in mathematical formulas **must be inside `\text{}`**, while variables, numbers, operators, and function names must be outside it. **Do not nest mathematical formulas inside `\text{}`**;

-   <span id="MATH-2.8">MATH-2.8</span>: in an `array` environment, **the actual number of columns must match the number of alignment specifiers**. For example, the data below has 3 columns (`&` separates columns), so it needs 3 alignment specifiers (`l`/`r`/`c` mean left/right/center alignment).

    ```latex
    $$
    \begin{array}{lll}
    F_1=\{\frac{0}{1},&&\frac{1}{1}\}\\
    F_2=\{\frac{0}{1},&\frac{1}{2},&\frac{1}{1}\}\\
    \end{array}
    $$
    ```

#### Pseudocode format

There are no strict requirements for the exact pseudocode format; consult Introduction to Algorithms or academic papers. Do not write it as Python.

<span id="PCOD-1">PCOD-1</span>: on the Wiki, write pseudocode in LaTeX, entirely inside an array environment. Use `$\qquad$` for indentation, `$\text$` for text descriptions, `$\textbf$` for keywords, `$\textit$` for multiletter variables, and `$\gets$` for assignment.

Example:

$$
\begin{array}{l}
\textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v, w) \\
\text{ denoting that there is an edge between } u \text{ and } v \text{ weighted } w . \\
\textbf{Output. } \text{The edges of the MST of the input graph}. \\
\textbf{Method. } \\
\begin{array}{ll} 
1 &  \textit{result} \gets \varnothing \\
2 &  \text{sort } e \text{ into nondecreasing order by weight } w \\ 
3 &  \textbf{for} \text{ each } (u, v, w) \text{ in the sorted } e \\ 
4 &  \qquad \textbf{if } u \text{ and } v \text{ are not connected in the union-find set } \\
5 &  \qquad\qquad \text{connect } u \text{ and } v \text{ in the union-find set} \\
6 &  \qquad\qquad \textit{result} \gets \textit{result}\;\bigcup\ \{(u, v, w)\} \\
7 &  \textbf{return } \textit{result}
\end{array}
\end{array}
$$

```latex
$$
\begin{array}{l}
\textbf{Input. } \text{The edges of the graph } e , \text{ where each element in } e \text{ is } (u, v, w) \\
\text{ denoting that there is an edge between } u \text{ and } v \text{ weighted } w . \\
\textbf{Output. } \text{The edges of the MST of the input graph}. \\
\textbf{Method. } \\
\begin{array}{ll} 
1 &  \textit{result} \gets \varnothing \\
2 &  \text{sort } e \text{ into nondecreasing order by weight } w \\ 
3 &  \textbf{for} \text{ each } (u, v, w) \text{ in the sorted } e \\ 
4 &  \qquad \textbf{if } u \text{ and } v \text{ are not connected in the union-find set } \\
5 &  \qquad\qquad \text{connect } u \text{ and } v \text{ in the union-find set} \\
6 &  \qquad\qquad \textit{result} \gets \textit{result}\;\bigcup\ \{(u, v, w)\} \\
7 &  \textbf{return } \textit{result}
\end{array}
\end{array}
$$
```

#### Code block formatting requirements

There are currently two types of code blocks: snippets and example problems.

For code snippets:

-   <span id="CODE-1.1">CODE-1.1</span>: if a snippet is short enough and does not need testing, you can edit it directly in the Markdown document.
-   <span id="CODE-1.2">CODE-1.2</span>: because code embedded in Markdown documents is hard to test automatically, we recommend inserting snippets in the format used for example-problem code. You can use [multifile compilation](https://github.com/OI-wiki/OI-wiki/pull/5729) or the [Snippet Sections](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippet-sections) syntax:

    Multifile compilation example: [bubble sort](https://github.com/OI-wiki/OI-wiki/blob/c35defebff6cea072d6cfeb359642f6fd84e66c7/docs/basic/bubble-sort.md?plain=1#L48). The text includes [bubble-sort\_1.cpp](https://github.com/OI-wiki/OI-wiki/blob/c35defebff6cea072d6cfeb359642f6fd84e66c7/docs/basic/code/bubble-sort/bubble-sort_1.cpp), while the test code is in [bubble-sort\_1.aux1.cpp](https://github.com/OI-wiki/OI-wiki/blob/c35defebff6cea072d6cfeb359642f6fd84e66c7/docs/basic/code/bubble-sort/bubble-sort_1.aux1.cpp).

    Snippet Sections example: [prefix sums](https://github.com/OI-wiki/OI-wiki/blob/c7cf6d6de13b44757f1d0528e952349beb921f8a/docs/basic/prefix-sum.md?plain=1#L37). The text does not need the testing part of [prefix-sum\_1.cpp](https://github.com/OI-wiki/OI-wiki/blob/c7cf6d6de13b44757f1d0528e952349beb921f8a/docs/basic/code/prefix-sum/prefix-sum_1.cpp), so only the main code snippet is inserted.

    **Note**: do not use the [Snippet Lines](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#snippet-lines) syntax.

    To improve code reuse, you can split code into header files and include them in different test programs. If the text needs the complete test code as a reference implementation for an example problem, also assemble it into single-file code in the text using Snippet Sections for easier reading. Example: [red-black tree](https://github.com/OI-wiki/OI-wiki/blob/3b721e22ea60d59a2687a9b10555263de7bdc2f0/docs/ds/rbtree.md?plain=1#L218-L231).

For example-problem code:

-   <span id="CODE-2.1">CODE-2.1</span>: example-problem code is included as `--8<-- "path"`, with all code stored at `path`. The path is usually `docs/主题/code/内容/内容_编号.cpp` (topic/content/content_number).

-   <span id="CODE-2.2">CODE-2.2</span>: when modifying example-problem code, make sure it is correct. Each example has a set of test data stored in `/docs/主题/examples/内容/内容_编号.in/ans` (topic/content/content_number).

If you need to add an example problem:

-   Add your example code to `docs/主题/code/内容` and give it a number. This `内容` (content) folder usually already contains one or more code files. For example, to modify the code for `dag.md`, the path is `docs/dp/code/dag`, where `dp` is the topic and `dag` is the content.

-   To add example code after all existing examples, continue the current numbering. For example, if `code/prefix-sum/prefix-sum_3.cpp` already exists, name your code `prefix-sum_4.cpp` and add it to `docs/basic/code/prefix-sum` for an example after the last one.

-   To add example code in the middle of an article, insert it and change the existing numbering. For example, if `prefix-sum_2.cpp` and `prefix-sum_3.cpp` exist and you want an example between the second and third, name your code `prefix-sum_3.cpp`, rename the original `prefix-sum_3.cpp` to `prefix-sum_4.cpp`, and **update the numbering in both the Markdown document and the test-data folder**.

-   **Do not forget to add a set of test data for your code to ensure it runs successfully.** Add the data to `docs/主题/examples/内容`, storing the input as `内容_编号.in` and the expected answer as `内容_编号.ans`.

-   Finally, you can add the code to the document. Add a code block and write `--8<-- "你的代码路径"` (your code path) directly inside it.

**OI Wiki** tests example-problem code across platforms. To ensure your code passes, follow these rules:

-   <span id="CODE-3.1">CODE-3.1</span>: your code must compile and run under C++14, C++17, and C++20.
-   <span id="CODE-3.2">CODE-3.2</span>: do not use nonstandard headers such as `<bits/stdc++.h>` or `<bits/extc++.h>`.
-   <span id="CODE-3.3">CODE-3.3</span>: expected-answer files must not contain extra spaces.
-   <span id="CODE-3.4">CODE-3.4</span>: do not use [alternative tokens](https://en.cppreference.com/w/cpp/language/operator_alternative#Alternative_tokens).
-   <span id="CODE-3.5">CODE-3.5</span>: when using [aggregate initialization](https://en.cppreference.com/w/cpp/language/aggregate_initialization), do not write `(object){args}` in place of `object{args}`.
-   <span id="CODE-3.6">CODE-3.6</span>: pay attention to the format when [overloading operators](https://en.cppreference.com/w/cpp/language/operators); for example, when overloading a comparison operator as a member function, do not omit the `const` qualifier.
-   <span id="CODE-3.7">CODE-3.7</span>: do not use macros such as `#define int long long`.
-   <span id="CODE-3.8">CODE-3.8</span>: if you need C-style [formatted input/output](https://en.cppreference.com/w/cpp/io/c#Formatted_input.2Foutput), pay special attention to format specifiers: `size_t` uses `%zu`, and `ptrdiff_t` uses `%td`. For example, code printing the size of an STL container should look like `printf("%zu", container.size());`.
-   <span id="CODE-3.9">CODE-3.9</span>: avoid `<chrono>` because the libstdc++ `<chrono>` library in the current test environment has a [BUG](https://github.com/actions/runner-images/issues/8659).
-   <span id="CODE-3.10">CODE-3.10</span>: `long` and `unsigned long` are 32-bit in some test environments and 64-bit in others. To ensure consistent behavior across platforms, avoid these two types and use [fixed-width integer types](../lang/var.md#定宽整数类型).
-   <span id="CODE-3.11">CODE-3.11</span>: nonstandard features such as `__gcd`, `__int128`, and the `__builtin_` family are not recommended. If you need them, ensure your code passes tests on every platform. For example, [this code](https://github.com/OI-wiki/OI-wiki/blob/4af83d6db6017f4c36db6d4a7583bbc3f6257484/docs/ds/code/tree-decompose/tree-decompose_1.cpp#L24-L47) provides a cross-platform implementation of `_Find_first()`, a libstdc++-specific member function of [std::bitset](../lang/csl/bitset.md).

Also follow [CONT-10](#CONT-10) to improve code readability.

## Illustrated examples

The requirements above may be hard to grasp, so the following images explain which formats to use and which to avoid:

### Example 1

![](./images/format-1.png)

Putting complex LaTeX formulas in display mode creates a balanced page layout. However, **OI Wiki** is primarily a Chinese-language site, so we want most key information (such as headings) in Chinese whenever possible, except for English proper names.

### Example 2

![](./images/format-2.png)

In more complex LaTeX formulas, pay attention to aligning equals signs. You can also improve the content with appropriate **links** to Wiki pages.

### Example 3

![](./images/format-3.png)

In general, list sources in a `## References and notes` section at the end of the article, adding a footnote after the relevant sentence rather than a direct link. Always avoid expressing code through LaTeX formulas: the two square brackets in the image are noncompliant. We recommend `dp(i,j)` or `dp_{i,j}`.

### Example 4

![](./images/format-4.png)

For **multiplication**, we usually use `\times` or `\cdot`; in special cases (such as convolution), we use `*` (or `\ast`). Headings are concise phrases, but the body should not be a collection of disconnected phrases. We recommend changing "two elements" in the image to "the principles of dynamic programming have the following two elements" to keep the text coherent. On the positive side, appropriate **ordered** lists organize content more clearly. Again, when a list item is a sentence, add **punctuation** at the end. Ordered lists usually use semicolons, with a period after the final item; unordered lists use periods throughout.

### Example 5

![](./images/format-5.png)

Appropriate **images** improve readability. **Pseudocode** describes an algorithm's steps conveniently and concisely, and is easier to understand than a directly pasted code template.

### Example 6

![](./images/format-6.png)

The same issue appears again: the heading is in English. There is also no period after the parentheses. In addition, although the display formula in the image has no parentheses, excessive nested subscripts make the innermost subscript very small and the formula unattractive. Replace `son_{now,i}` with `son(now,i)` or `f_{now}` with `f(now)`. Try to keep nested subscripts and superscripts within two levels (for repeatedly nested superscripts, use Knuth's arrows, for example $2 \uparrow (2 \uparrow (2 \uparrow (2 \uparrow \cdots)))$ rather than $2^{2^{2^{2^{\cdots}}}}$, as in the problem "The Seven Minutes God Spent Creating Problems").

### Example 7

![](./images/format-7.png)

Use MkDocs extensions to separate example-problem statements from algorithm descriptions. Collapsing code makes an article more compact. (After all, most Wiki readers want to understand the idea; apart from templates that need to be read, most exercise code can be collapsed.) Both inline code and LaTeX formulas work well when describing function operations.

### Example 8

![](./images/format-8.png)

Listing references at the end of an article makes its content more rigorous and credible.

## External links

-   [General rules for punctuation (GB/T 15834—2011)](http://www.moe.gov.cn/jyb_sjzl/ziliao/A19/201001/W020190128580990138234.pdf)
-   [Wikipedia: Manual of Style/Punctuation](https://zh.wikipedia.org/wiki/Wikipedia:%E6%A0%BC%E5%BC%8F%E6%89%8B%E5%86%8C/%E6%A0%87%E7%82%B9%E7%AC%A6%E5%8F%B7)
-   [Chinese copywriting guidelines (Simplified Chinese edition)](https://mazhuang.org/wiki/chinese-copywriting-guidelines/)
-   [Chinese copywriting style guide - PDFE GUIDELINE](https://pdfe.github.io/GUIDELINE/#/others/copywriter)
-   [The (Not So) Short Introduction to LATEX2ε, or LATEX2ε in 106 Minutes](https://github.com/CTeX-org/lshort-zh-cn/releases)
-   [Editorial guidelines for English in Chinese publications](https://www.nppa.gov.cn/xxgk/fdzdgknr/hybz/202210/t20221004_445147.html)

## References and notes

[^note1]: The colon here summarizes the preceding text.

[^note2]: Use an English comma between a full English scientific or technical name and its abbreviation. An English sentence or passage inserted into a Chinese sentence as a note, supplement, or explanation should be enclosed in Chinese parentheses.

[^note3]: Collapsible blocks: see [Collapsible Blocks](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#collapsible-blocks). We sometimes call this "Details syntax" because its functionality matches the HTML [`<details>` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details).

[^note4]: Moved to [How to contribute](./htc.md).

[^note5]: This rule was added to [Before editing](../edit-landing.md) and announced, but was not added to this document.

[^note6]: Tabs: see [Content tabs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs).

[^ref1]: [cstdio stdio.h namespace](https://stackoverflow.com/questions/10460250/cstdio-stdio-h-namespace)

[^ref2]: [CCF announcement on the resumption of NOIP - China Computer Federation](https://www.ccf.org.cn/c/2020-01-21/694716.shtml)

[^ref3]: [Why does my formula display incorrectly in the table of contents? It seems doubled](faq.md)

[^ref4]: [SVG|MDN](https://developer.mozilla.org/zh-CN/docs/Web/SVG)

[^webarchive]: [Save Page in Internet Archive](https://web.archive.org/save/)

[^apng]: [APNG](https://en.wikipedia.org/wiki/APNG)

[^intro-apng]: [OI-wiki/OI-wiki#3422](https://github.com/OI-wiki/OI-wiki/issues/3422)
