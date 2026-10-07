---
title: How to contribute
---

Before this article begins, every member of the **OI Wiki** project team warmly welcomes you to contribute pages to this project. It is thanks to hundreds of people like you that **OI Wiki** has become what it is today!

This article mainly describes the writing process for contributing to **OI Wiki**. Before writing or correcting wiki pages, please read the following carefully to help you produce higher-quality content.

## Contribution guidelines

Before editing, read the [OI Wiki contribution guidelines](https://github.com/OI-wiki/OI-wiki/blob/master/.github/CONTRIBUTING.md) and [project guidelines](./about.md#project-guidelines) to collaborate and communicate more effectively with community contributors.

## Collaboration

???+ warning "Warning"
    Before starting to write a piece of content, check the [Issues](https://github.com/OI-wiki/OI-wiki/issues), confirm that nobody is already doing the same work, and open a [new issue](https://github.com/OI-wiki/OI-wiki/issues/new) describing the content you plan to write.

???+ tip "Tip"
    There are also many problems to fix or resolve among the issues, especially in our Iteration Plan. Picking a task from there is a great place to start!

To ensure that articles are accurate and well informed, we recommend considering the following before editing:

1.  **Choose an area you know**: prioritize articles related to your expertise, educational background, or interests. This helps you create high-quality content.
2.  **Approach new areas cautiously**: if you are a beginner in a topic or do not know it well, deepen your understanding through reading and learning first, and only start editing when you feel reasonably confident.
3.  **Consult relevant sources**: when adding or revising content, consult authoritative literature and sources first to ensure accuracy. You are also welcome to ask questions in the page comments or our community and discuss them with other editors.

We value every contributor's enthusiasm and effort, and understand that everyone's level of expertise differs. Let us work together to care for this haven of knowledge and help more readers with accurate, informed content. We look forward to your contributions! To quote Wikipedia:

> Do not be afraid to edit; be bold in updating pages![^ref1]

### Editing on GitHub

Contributing to **OI Wiki** **requires** a GitHub account (you can register on [GitHub's signup page](https://github.com/signup)), but **does not require** advanced GitHub skills. Even a beginner can do an **excellent** job of editing by following the steps below.

???+ tip "Tip"
    Until your changes are merged into the main **OI Wiki** repository, none of your edits will appear on the main **OI Wiki** website, so you do not need to worry about breaking the content currently displayed on **OI Wiki**.
    
    If you are still unsure, see [GitHub's official tutorials](https://skills.github.com/).

#### Editing the content of a single page

1.  Find the corresponding page on **OI Wiki**;
2.  click the **"Edit this page"** (<i class="md-icon">edit</i>) button at the top right of the article (to the left of the table of contents). After confirming that you have read this page and the [Style guide](./format.md), click the button and follow the prompts to edit on GitHub;
3.  write your changes in the editor. When editing and subsequently submitting changes, **turn off your automatic translation software**, since it can cause unnecessary problems (for example, it may incorrectly rename a file you are editing and disrupt the directory structure);
4.  when you finish writing, scroll to the bottom of the page and enter a commit message following the [Commit message format](#commit-message-format) section, then click **Propose changes** to submit your changes. GitHub will automatically create a fork of the **OI Wiki** repository for you and add your commit to it.
5.  GitHub will automatically open your fork's page. A green **Create pull request** button will appear at the top. Click it to open the pull request creation page. Scroll down and check your changes for mistakes, write the pull request description according to the [Pull request format](#pull-request-format) section, and click the green **Create pull request** button to create the pull request.
6.  If all goes well, your pull request has been submitted successfully. Wait for the administrators to review it and merge it into the main repository.

While waiting for the merge, you can comment on, upvote, or downvote other people's pull requests. New messages will generate a notification in the upper-right corner of the page, along with an email notification (depending on the notification settings in your personal preferences).

#### Editing the content of multiple pages

If you need to edit several unrelated pages at the same time, follow the [Editing the content of a single page](#editing-the-content-of-a-single-page) section above and modify all the pages in one go.

1.  Open the [OI-Wiki/OI-Wiki](https://github.com/OI-Wiki/OI-Wiki) repository and press <kbd>.</kbd> (or replace `github.com` in the URL with `github.dev`)[^ref2] to enter GitHub's web-based VS Code editor;
2.  edit the source files in the editor. Use the preview button at the top right (or the <kbd>Ctrl+K</kbd><kbd>V</kbd> shortcut) to open a preview on the right;
3.  after editing, use the Source Control tab on the left, enter a commit message following the [Commit message format](#commit-message-format) section, and commit. When asked whether to create a fork of this repository, click the green **Fork Repository** button.
4.  After committing, a dialog will appear at the top center of the page. Enter a title in the first dialog and the destination branch name in the second. A notification such as `Created Pull Request #1 for OI-Wiki/OI-Wiki.` will then appear in the lower-right corner. Click the blue link to view that pull request.

#### Adding changes to a pull request

1.  Open the [OI Wiki pull request list](https://github.com/OI-wiki/OI-wiki/pulls), find your pull request, and click it.
2.  Below the pull request title, you will see text such as `<yourID> wants to merge x commits into OI-wiki:master from <yourID>:patch-1`. Click the `<yourID>:patch-1` part.
3.  You should be redirected to your fork, with the branch name at the top left of the file list set to the branch from which you submitted the pull request (`patch-1` in this example).
4.  Make the changes you need.
    -   To edit a single file or several unrelated pages, find the file and make your changes. Then scroll to the bottom, enter a commit message following the [Commit message format](#commit-message-format) section, and click **Commit changes** to submit them.
    -   To edit multiple files, press <kbd>.</kbd> (or replace `github.com` in the URL with `github.dev`)[^ref2] to enter GitHub's web-based VS Code editor and make your changes. Then use the Source Control tab on the left, enter a commit message following the [Commit message format](#commit-message-format) section, and commit the changes.
5.  Your changes will automatically be added to your pull request.

### Editing locally with Git

???+ warning "Warning"
    For most users, we recommend the GitHub web editor described above.

Although you can edit directly on GitHub in most cases, we recommend editing locally with Git in special situations, such as when GPG signatures are required.

The general workflow is:

1.  fork the main repository to your account;
2.  clone your fork locally;
3.  make local changes and commit them;
4.  push the changes to the fork you cloned;
5.  submit a pull request to the main repository.

For detailed instructions, see the [Git](../tools/git.md) page.

#### Adding changes to a pull request

Continue making changes in your locally cloned fork, then commit and push them. Your changes will automatically be added to the pull request.

### Previewing changes on the built website

You can find the test page near the bottom of the pull request page. Click the Details link for netlify/oi-wiki/deploy-preview (as shown below) to open an automatically built preview of the page with your changes.

![deploy\_preview](./images/deploy_preview.png)

### Changes to navigation and links

Usually, to add a new page or change an existing page's link in the navigation, you need to modify [`mkdocs.yml`](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml).

Follow the existing format when adding a page. However, unless you are restructuring or correcting terminology, **we do not recommend changing links to existing pages**. Unnecessary changes in pull requests will be rejected.

If you insist on changing a link, remember to update the author field and the redirects file.

### The author field

The GitHub API cannot track statistics after a file's path changes, so we manually maintain an author list at the start of the file to address this. The author field appears at the very beginning of the Markdown file, in a form such as `author: Ir1d, cjsoft`, with adjacent IDs separated by a comma and a space. An ID is a GitHub username, the relevant part of a GitHub profile URL (for example, `Ir1d` in <https://github.com/Ir1d>).

When changing a link, add all of the current page's contributors to the author field.

### The redirects file

When changing links, update the redirects file to prevent external references from becoming dead links.

The [`_redirects`](https://github.com/OI-wiki/OI-wiki/blob/master/docs/_redirects) file is used to generate the [Netlify configuration](https://docs.netlify.com/routing/redirects/#syntax-for-the-redirects-file) and [redirect files](https://github.com/OI-wiki/OI-wiki/blob/master/scripts/gen_redirect.py).

Each line specifies a redirect rule, giving the source and destination URLs (without the domain name):

```text
/path/to/src /path/to/desc
```

Note: all redirects are 301 redirects. Changes are only necessary when URL changes in the navigation cause dead links.

### Commit message format

Follow these basic requirements when writing a commit message:

1.  briefly describe the changes in the commit summary. Keep the summary within 50 characters; any excess will automatically be placed in the body.
2.  If more explanation is needed, describe the commit in detail in the body.

The recommended format for a commit summary is:

```text
<change type>(<file name>): <description of changes>
```

Change types are as follows:

-   `feat`: adding content.
-   `fix`: correcting errors in existing content.
-   `refactor`: restructuring a page (large-scale changes).
-   `revert`: reverting earlier changes.

### Pull request format

Follow these requirements for pull requests:

1.  clearly state the PR's purpose in the title (**what** work was done, **which** problem was fixed).
2.  Briefly describe the changes in the body. If the PR fixes an issue, add `fix #xxxx`, where `xxxx` is the issue number.
3.  Carefully read the [contribution guidelines](https://github.com/OI-wiki/OI-wiki/blob/master/.github/CONTRIBUTING.md) and [code of conduct](https://github.com/OI-wiki/OI-wiki/blob/master/CODE_OF_CONDUCT.md). If you agree, check the boxes in the PR template to confirm your agreement.

The recommended format for a pull request title is:

```plain
<change type>(<file name>): <description of changes> (<corresponding issue number>)
```

Change types are as follows:

-   `feat`: adding content.
-   `fix`: correcting errors in existing content.
-   `refactor`: restructuring a page (large-scale changes).
-   `revert`: reverting earlier changes.

Examples:

-   `fix(ds/persistent-seg): clarify descriptions in code comments`
-   `fix: tools/judger/index is missing from the navigation (#3709)`
-   `feat(math/poly/fft): better proof`
-   `refactor(ds/stack): organize page content`

### Collaboration workflow

1.  When a new pull request is received, GitHub emails the reviewers;
2.  at the same time, two sets of tests run on [GitHub Actions](https://github.com/OI-wiki/OI-wiki/actions) and [Netlify](https://app.netlify.com/sites/oi-wiki), with progress shown at the bottom of the PR page. GitHub Actions mainly checks that the PR's changes do not disrupt the website build; Netlify builds a preview of the changes for reviewers (click Details after the tests finish for more information);
3.  reviewers may find problems and submit a `review`, `suggested changes` (shown with a gray icon), or `requested changes` (mandatory changes, shown with a red icon and available only to reviewers with write access to the repository). Reviewers usually include suggestions and required changes, so you will need to add further changes to the pull request. See "Adding changes to a pull request" under "Editing on GitHub" or "Editing locally with Git" for instructions.
4.  Only after enough reviewers approve a PR can it be merged into the master branch;
5.  after merging into master, GitHub Actions rebuilds the website content and updates the gh-pages branch;
6.  only then does the server fetch the updates from gh-pages and redeploy the latest content.

## References and notes

[^ref1]: [Wikipedia: Introduction/Editing](https://zh.wikipedia.org/wiki/Wikipedia:%E6%96%B0%E6%89%8B%E5%85%A5%E9%96%80/%E7%B7%A8%E8%BC%AF)

[^ref2]: [Web-based editor - GitHub Codespaces - GitHub Docs](https://docs.github.com/en/codespaces/developing-in-codespaces/web-based-editor)
