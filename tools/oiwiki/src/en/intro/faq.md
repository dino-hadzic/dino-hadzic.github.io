---
title: F.A.Q.
---

This page answers some frequently asked questions.

## I would like to ask something about this Wiki

Q: Why did you want to make this Wiki in the first place?

A: I don't know whether, while learning **OI**, you have ever felt lost and helpless in the face of the huge body of knowledge. What **OI Wiki** wants to do could be described roughly as "making it easy for more students without sufficient competition resources to get access to training materials". Of course, that description is not complete either; the motivation for the Wiki may also be quite pure – simply the wish to make a small contribution to the development of **OI**. XD

***

Q: I'm interested, how can I get involved?

A: **OI Wiki** is now hosted on GitHub; you can follow the latest progress directly in this [repo](https://github.com/OI-wiki/OI-wiki). Ways to participate include opening an [Issue](https://github.com/OI-wiki/OI-wiki/issues) or a [Pull Request](https://github.com/OI-wiki/OI-wiki/pulls) on GitHub, sharing your ideas in the discussion groups, or submitting contributions directly to the administrators. Currently we use the framework [MkDocs](https://mkdocs.readthedocs.io), developed in Python, which supports Markdown (including math formulas).

***

Q: But I'm rather weak… I don't know what I could do.

A: Everything starts with passion. You can help others review and revise contributions, help us promote **OI Wiki**, and help create a good atmosphere of learning and exchange in the community!

***

Q: Who is mainly working on this now? It looks like a huge undertaking – can it really be done well?

A: At the beginning it was mainly some retired senior contestants, and later we met many like-minded people: active contestants, former contestants, and also friends who have never taken part in **OI**. Currently the project is mainly maintained by the **OI Wiki** project team (below is a group photo).

<a href="https://github.com/OI-wiki/OI-wiki/graphs/contributors"><img src="https://opencollective.com/oi-wiki/contributors.svg?width=890&button=false"/></a>

Of course, it is hard to make this project perfect with our strength alone, so we sincerely invite you to improve **OI Wiki** together with us.

***

Q: How do you guarantee that the content we add won't suddenly disappear?

A: We host the content on [GitHub](https://github.com/OI-wiki/OI-wiki), so even if our server crashes, the content will not be lost. In addition, we regularly back up everyone's hard work, so even if GitHub goes out of business one day (?), our content will not be lost.

***

Q: **OI Wiki** seems to have empty pages!

A: Yes. Limited by the skills and time of the team members, we are unable to complete these empty pages for now. That is why we are soliciting contributions and recruiting here, hoping to meet friends with the same ideas so that we can improve **OI Wiki** together.

***

Q: Why not just write on the [Chinese Wikipedia](https://zh.wikipedia.org/)?

A: Because we hope to really help more contestants and people interested in this content. Moreover, for well-known reasons, the content of the Chinese Wikipedia cannot be accessed without obstacles.

## I want to get involved!

Q: How do I communicate with the project team?

A: You can contact us through the [ways to get in touch described in the About page](./about.md#how-to-get-in-touch).

***

Q: How do I contribute code or content?

Please refer to the page [How to contribute](./htc.md).

***

Q: Where is the table of contents?

A: The table of contents is in the file [mkdocs.yml](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml#L17) in the project root.

***

Q: How do I modify the content of a topic?

A: There is an edit button<i class="md-icon">edit</i> in the upper right corner of the corresponding page; after clicking it and confirming that you have read [How to contribute](./htc.md), you will be redirected to the corresponding file on GitHub.

Alternatively, you can read the table of contents [(mkdocs.yml)](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml) yourself to find the file location.

***

Q: How do I add a topic?

A: There are two options:

-   You can open an Issue stating the content you would like to add.
-   You can open a Pull Request: add the new topic to the table of contents [(mkdocs.yml)](https://github.com/OI-wiki/OI-wiki/blob/master/mkdocs.yml) and create an empty `.md` file at the corresponding location in the [docs](https://github.com/OI-wiki/OI-wiki/tree/master/docs) folder. For details on the document format, see the [format manual](./format.md#requirements-for-documentation-contributions).

***

Q: I have trouble accessing GitHub.

A: We recommend adding the following lines to your hosts file[^ref1]:

```text
# GitHub Start
140.82.114.25                 alive.github.com
140.82.113.5                  api.github.com
185.199.110.153               assets-cdn.github.com
185.199.111.133               avatars.githubusercontent.com
185.199.111.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.111.133               avatars3.githubusercontent.com
185.199.111.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.111.133               camo.githubusercontent.com
140.82.112.22                 central.github.com
185.199.111.133               cloud.githubusercontent.com
140.82.114.9                  codeload.github.com
140.82.113.22                 collector.github.com
185.199.111.133               desktop.githubusercontent.com
185.199.111.133               favicons.githubusercontent.com
140.82.112.3                  gist.github.com
52.216.163.147                github-cloud.s3.amazonaws.com
52.217.124.1                  github-com.s3.amazonaws.com
52.216.144.83                 github-production-release-asset-2e65be.s3.amazonaws.com
52.217.121.249                github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.206.57                 github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
140.82.114.4                  github.com
140.82.113.18                 github.community
185.199.110.154               github.githubassets.com
151.101.1.194                 github.global.ssl.fastly.net
185.199.110.153               github.io
185.199.111.133               github.map.fastly.net
185.199.110.153               githubstatus.com
140.82.112.25                 live.github.com
185.199.111.133               media.githubusercontent.com
185.199.111.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.111.133               raw.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
13.107.253.40                 vscode.dev
140.82.112.21                 education.github.com
# GitHub End
```

You can find the latest data and more information at [GitHub520](https://gitee.com/klmahuaw/GitHub520).

Linux and macOS users can try the [gh-check script](https://gist.github.com/lilydjwg/93d33ed04547e1b9f7a86b64ef2ed058) by [依云 (lilydjwg)](https://github.com/lilydjwg/) to find the fastest IP; the `--hosts` option updates the hosts file directly, and the `--help` option prints usage help. Before using it you need to install Python 3 and aiohttp (`pip install aiohttp -i https://pypi.tuna.tsinghua.edu.cn/simple/`). The author's blog post: [Finding the fastest GitHub IP (Chinese)](https://blog.lilydjwg.me/2019/8/16/gh-check.214730.html).

You can also use the [Gitclone](https://www.gitclone.com/) service to speed up cloning; see the instructions on its home page.

If you only want to clone the **OI Wiki** repository:

```bash
git clone https://gitclone.com/github.com/OI-wiki/OI-wiki
```

If you want to contribute to **OI Wiki**, first fork the **OI Wiki** repository, then (replace `username` with your user name); note that the example given will make you connect to GitHub via SSH[^only-ssh-connect]:

```bash
git clone https://gitclone.com/github.com/username/OI-wiki
git remote set-url origin git@github.com:username/OI-wiki.git
```

***

Q: My pip is way too slow!

A: You can switch to a Chinese mirror[^ref2], or:

```bash
pip install -U -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

***

Q: I cloned the project with a client and it's too slow.

A: If you have `git bash` installed, you can add a few restrictions to reduce the download size.[^ref3]

```bash
git clone https://github.com/OI-wiki/OI-wiki.git --depth=1 -b master
```

***

Q: I have never installed Python 3.

A: See the [official Python website](https://www.python.org/downloads/) for more information.

***

Q: It seems to tell me my pip version is too old.

A: Open cmd/shell and run the following command:

```bash
python -m pip install --upgrade pip
```

***

Q: Installing the dependencies failed.

A: Check: network? permissions? the error message?

***

Q: I have already cloned it, why can't I deploy it?

A: Check whether the dependencies are installed.

***

Q: I cloned the repo a long time ago; how do I update to the new version?

A: Please refer to GitHub's official help page [Syncing a fork - GitHub Docs](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork).

***

Q: How do I update previously installed dependencies?

A: Enter the following command:

```bash
pip install -U -r requirements.txt
```

***

Q: Why is my Markdown formatting broken?

A: See [cyent's notes (Chinese)](https://web.archive.org/web/20221103014610/https://cyent.github.io/markdown-with-mkdocs-material/) or the [MkDocs usage notes (Chinese)](https://github.com/ctf-wiki/ctf-wiki/wiki/Mkdocs-%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E).

We currently use [remark-lint](https://github.com/remarkjs/remark-lint) to fix the formatting automatically; there may still be places where the [configuration](https://github.com/OI-wiki/OI-wiki/blob/master/.remarkrc) is not good enough, and you are welcome to point them out.

***

Q: Is it true that GitHub does not display my math formulas?

A: Yes, GitHub's preview does not display math formulas. But rest assured, MkDocs supports math formulas and they work fine; anything supported by MathJax can be used.

***

Q: Why is my formula garbled?

A: If it is a display formula (using `$$`), the known issue is that there must be blank lines around `$$`, and `$$` must be placed **alone** on a line (with no leading spaces). The format is as follows:

```text
// blank line
$$
a_i
$$
// blank line
```

***

Q: Why isn't my formula displayed correctly in the table of contents? It looks doubled.

A: Yes, this is a bug in python-markdown that may be fixed soon.

If you want to avoid doubled formulas in the table of contents, see [how the headings of the SAM page in the string category are written](https://github.com/OI-wiki/OI-wiki/blame/master/docs/string/sam.md#L73).

```text
结束位置 <script type="math/tex">endpos</script>
```

In the table of contents this becomes

```text
结束位置 endpos
```

Note: please now avoid MathJax formulas in headings that appear in the table of contents whenever possible.

***

Q: How do I declare copyright information for a single page?

A: Just add one line at the beginning of the page.[^ref4]

For example:

```text
copyright: SATA
```

Note: the default is CC BY-SA 4.0 and SATA.

***

Q: Why isn't my name in the author statistics?

A: If you find that you wrote part of a page but you are not recorded in the author list, add your GitHub ID to the [author field](./htc.md#the-author-field) in the file header.

***

Thank you for reading to the end. What we urgently need right now is your help.

The **OI Wiki** project team

2018.8

## References and notes

[^ref1]: [GitHub520](https://gitee.com/klmahuaw/GitHub520)

[^ref2]: [Changing the pip source to a Chinese mirror - L 瑜 - CSDN blog (Chinese)](https://blog.csdn.net/lambert310/article/details/52412059)

[^ref3]: [GIT – step-by-step for beginners (Windows Git Bash) (Chinese)](https://blog.csdn.net/FreeApe/article/details/46845555)

[^ref4]: [Metadata - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/extensions/metadata/#usage)

[^only-ssh-connect]: GitHub has deprecated password-based HTTPS authentication, so connections must use SSH or a Personal Access Token; see [Which remote URL should I use?](https://docs.github.com/cn/github/using-git/which-remote-url-should-i-use), [Creating a personal access token](https://docs.github.com/cn/github/authenticating-to-github/creating-a-personal-access-token) and [Connecting to GitHub with SSH](https://docs.github.com/cn/github/authenticating-to-github/connecting-to-github-with-ssh).
