---
title: OI contests and contest formats
---

## Introduction to the contests

The **Olympiad in Informatics** (abbreviated OI) is a subject competition widely held among secondary-school students, of the same nature as competitions in physics, mathematics and so on. OI tests the contestants' ability to solve practical problems by writing computer programs, using algorithms, data structures and mathematical knowledge.

There are many kinds of OI contests; in China alone they include:

-   the National Olympiad in Informatics in Provinces (NOIP)
-   the National Olympiad in Informatics (NOI)
-   the National Olympiad in Informatics Winter Camp (WC)
-   the China Team Selection Competition for the International Olympiad in Informatics (CTSC)

International OI contests include:

-   the International Olympiad in Informatics (IOI)
-   the USA Computing Olympiad (USACO)
-   the Japanese Olympiad in Informatics (JOI)
-   the Asia-Pacific Informatics Olympiad (APIO)

    …

For most contestants, each year's new season begins with the first round of CSP-J/S in September.

In China, the only language allowed in OI contests is C++ (C and Pascal were once allowed too, but support for both has been discontinued). Different contests have different rules regarding the C++ version. The problems are generally related to algorithms or data structures, and the problem forms include traditional problems (the most common form, with input and output through files) and non-traditional problems (output-only problems, interactive problems, code-completion problems, etc.).

## Introduction to the contest formats

### OI format

Contestants have only one chance to submit. Judging results cannot be seen during the contest; scores are published after the contest. Each problem has several test cases, and points are awarded according to the number of test cases passed in each problem; each test case may also carry partial credit, so points can be earned even if only part of the data passes.

???+ note "The self-evaluation tool selfEval"
    Nowadays, some NOI-series contests provide the self-evaluation tool selfEval. selfEval is built into the national-contest edition of NOI Linux. Since it was officially announced and put into use at NOI 2023, selfEval has been used successively at later NOI national contests, APIO (China region), the NOI Winter Camp and others. Contestants can use selfEval to test their programs on a set of test data (called pretest data) and receive feedback. The number of self-tests per contest has a specified upper limit (50 at NOI 2024, 30 at NOI 2025), and the pretest data is also invisible to contestants. Since the pretest data differs from the official test data, self-test results are only for debugging and cannot be regarded as official judging results. When a contestant pretests the same problem several times, the pretest data used is the same.

The second round of CSP-J/S, NOIP, the provincial selections and NOI all use the OI format.

### IOI format

Contestants have multiple chances to submit during the contest. Submissions are judged in real time and the results are returned; there is no penalty if a submission is wrong. Each problem has several test cases, and points are awarded according to the number of test cases passed in each problem.

APIO and IOI both use the IOI format. Domestic contests are currently also gradually moving toward the IOI format.

### Codeforces (CF) format

[Codeforces](https://codeforces.com) is an online judge that regularly holds contests.

Its contests are characterized by testing only part of the data during the contest (Pretests) and returning the full results on all test cases after the contest ends (System Tests). Multiple submissions are allowed during the contest, and hacking other people's code is permitted (hacking here means submitting a test case on which someone else's code fails to give the correct answer). To hack, a contestant must lock their own code (in other words, that problem can no longer be resubmitted during the contest). When hacking, copying the contestant's program to a local machine for testing is not allowed; the source code is converted into an image.

Codeforces also offers another format, called Extended ICPC (or ICPC+). In this format, all data is tested during the contest, but after the contest there is a 12-hour open hacking phase for everyone. When hacking, copying the contestant's program to a local machine for testing is allowed.

## Major contests

### CSP-J/S

**CSP-J/S** (Certified Software Professional Junior/Senior) is the non-professional software capability certification test launched by CCF after NOIP was cancelled in 2019. Before 2025 it was open to all ages, and [it was later restricted to those aged 12 and above](https://www.noi.cn/xw/2025-02-13/837984.shtml).

CSP-J/S is divided into an entry level (Junior, abbreviated CSP-J) and an advanced level (Senior, abbreviated CSP-S), and the schedule consists of a first round (usually in September each year) and a second round (usually in October each year). The first round is a written test covering computer theory, general knowledge of computer operation, and basic algorithms and mathematics; the second round is an on-computer test with 4 problems in both the entry and advanced groups, where the entry group has 3.5 hours and the advanced group 4 hours (except CSP-S 2019, which used the old NOIP advanced-group format with two days, 3 problems and 3.5 hours per day). The first round is open to all students aged 12 and above, and after a ranking-based selection, those with excellent results get the chance to participate in the second round.

Registering for the first/second round and filing problem appeals after the second round all require paying a fee to CCF.

In both rounds, contestants' results are certified by rank on a per-province basis, in three grades: first, second and third.

### NOIP

**NOIP** (National Olympiad in Informatics in Provinces) is an informatics competition organized by the People's Republic of China for secondary-school students in China (including Hong Kong and Macau).

The old format up to and including 2018: NOIP was divided by participants into the popularization group and the advanced group, and in 2018 an entry group was piloted in Shanghai; by stage it was divided into the preliminary round and the final round. The preliminary round tested basic computer knowledge and algorithm fundamentals, and the final round was an on-computer test. It was generally held on the second weekend of November: Saturday morning the first advanced-group session 8:30–12:00 (3.5 hours, 3 problems), Saturday afternoon 14:30–18:00 the popularization group (3.5 hours, 4 problems), Sunday morning the second advanced-group session 8:30–12:00 (3.5 hours, 3 problems). The same problem set was used nationwide, but the award rules were set uniformly by CCF (China Computer Federation) according to the situation within each province and published after the contest on the [official NOI website](http://www.noi.cn). The first-prize score thresholds differed slightly between provinces.

NOIP was [suspended by CCF](http://www.noi.cn/xw/2019-08-16/715365.shtml) on August 16, 2019, and [announced to be restored](http://www.noi.cn/xw/2020-01-21/715520.shtml) on January 21, 2020. The NOIP format from 2020 onward differs from before, as follows:

-   the preliminary round is cancelled and replaced by the first round of CSP-J/S;
-   the popularization group is cancelled and replaced by CSP-J, so since then NOIP has only one group, aimed at advanced-level contestants;
-   the schedule is shortened from the previous two days with 6 problems in total and 3.5 hours per day to one day with 4 problems in 4.5 hours in total;
-   contestants must achieve a certain rank in the second round of CSP-S to qualify for NOIP; the specific quotas vary by province. A province's NOIP qualification quota depends on the number of participants and results of that province in the previous season, among other things.

Registering for NOIP and filing problem appeals do not require additional fees.

NOIP is ranked and awarded on a per-province basis. As of 2019, contestants who won a provincial first prize in the advanced group could obtain eligibility for independent admission at most universities.

> In January 2020, the Ministry of Education of the People's Republic of China issued the [Opinions on Piloting the Reform of Admissions in Basic Disciplines at Some Universities](http://www.moe.gov.cn/srcsite/A15/moe_776/s3258/202001/t20200115_415589.html). The opinions state that from 2020 onward, universities will no longer organize independent admissions, and that a pilot reform of admissions in basic disciplines (the Qiangji Plan) will be carried out at some first-class universities.

### Provincial selection

The **provincial selection** (abbreviated 省选) is used to select each province's team for the national contest and is generally held between January and April each year. The schedule usually spans two days, with 3 problems in 4.5 hours each day.

The problems of the provincial selection are decided by each province itself; the current trend is that many provinces choose to set problems jointly.

The quota of each provincial team follows complicated formulas, generally related to previous results and the number of participants. Usually, NOIP scores must account for a certain proportion of the provincial selection criteria. According to the rules, junior-high contestants can only be selected as class E contestants and cannot take part in the class A and B selection. Class A has 5 contestants ([at least 1 female](https://www.noi.cn/xw/2024-08-26/829152.shtml)), and the other contestants enter team B in order according to the given quota and their scores. The number of NOI participants from a single school may not exceed one third (rounded) of the province's total A and B quota, and the highest-scoring female contestant selected into team A does not count toward this proportion (known as the 1/3 limit or 1/3 elimination; see the [official CCF explanation](https://www.noi.cn/xw/2022-12-14/781364.shtml)).

Since 2020, the NOI provincial team selection has been set and judged uniformly by CCF; provinces capable of setting problems may do so themselves, but the selection method must be approved by CCF. Since 2024, the NOI provincial team selection has returned to independent problem setting by each province; provinces that need to may organize joint contests or use other provinces' problems, but the specific plan must be approved by CCF.

### NOI

**NOI** (National Olympiad in Informatics) is the highest-level domestic contest for provincial teams, including Hong Kong and Macau.

NOI is generally held in July, and contestants are divided into official contestants and summer-camp contestants. Official contestants are further divided into three classes: classes A and B are official provincial-team contestants, and class C contestants are invitational contestants. Classes A and B correspond to the A and B classes of the provincial teams (class A receives a 5-point bonus when results are computed); class C is nominally a reward quota for schools that have made outstanding contributions to CCF. Summer-camp contestants are divided into classes D and E, corresponding to unofficial contestants in the senior-high and junior-high groups respectively. If summer-camp contestants exceed the score threshold, they only receive a certificate of results rather than a medal (the same score carries somewhat less weight). The top 50 official contestants form the national training team and obtain eligibility for guaranteed university admission.

On the international stage, to distinguish it from other contests also called NOI, it is sometimes referred to as CNOI.

### CTT

**CTT** (China Team Training) is the training and selection event held every winter for members of the IOI national training team, consisting of 3–4 tests. Besides the national training team, some contestants who achieved excellent results at that year's NOI may also take part in CTT under the name of "elite training".

CTT, together with homework and other procedures, constitutes the first stage of national team selection. Since 2021, the top 30 contestants in the first stage become the national candidate team and enter the second stage of selection (WC).

### WC

**WC** (Winter Camp, the National Olympiad in Informatics Winter Camp) is an event held every winter at the venue of that year's NOI. Although the event is mainly used for training-team training and national team selection, contestants who achieved good results in the previous year's NOIP and second round of CSP-S can also participate as unofficial campers.

WC consists of several days of training and tests, and the test results are combined with the results of the previous stages to compute the overall ranking of the training-team contestants. Before 2020, there was only one test, with the same problems for the training team and the unofficial campers, and the top 15 training-team contestants by overall result became the national candidate team and took part in the final stage of selection (CTS, etc.); since 2021, with the national team selection function of CTS merged into WC, the candidate team takes two tests while the unofficial campers still take one, and the unofficial campers' problems partly overlap with the candidate team's problems. The top 6 candidates by overall ranking proceed to the final interview, from which 4 official contestants and 2 reserve contestants are selected for that year's IOI.

### APIO

**APIO** (Asia-Pacific Informatics Olympiad) is an informatics competition for secondary-school students in the Asia-Pacific region. CCF holds a mirror contest for the China region at the beginning of May each year. Training activities are held around the contest day.

APIO contestants are divided into class A and class B: the top six in class A (including ties) may take part in the APIO international award selection, while class B contestants may only take part in the China-region award selection.

### CTS

**CTS** (formerly CTSC, China Team Selection Competition) is used to select the national team (6 people) from the national candidate team (15 people) in preparation for that summer's IOI, with 4 official contestants and 2 reserve contestants. As with WC, contestants who achieved good results in the previous year's NOIP may also participate (without taking part in the selection).

Registration for APIO and CTS is done by province, and the participants in APIO and CTS are generally determined by the NOIP ranking (the two are usually very close in time).

CTS 2020 was cancelled because of the pandemic, and that year's national training team was selected through NOI; since 2021, the CTS selection process has been replaced by WC.

### IOI

**IOI** (International Olympiad in Informatics) is an annual informatics competition for secondary-school students worldwide. Each country sends four contestants, and the contest is usually livestreamed. In the IOI format each problem has subtasks, and each subtask corresponds to a certain number of points.

### University camps

#### Peking University (PKU)

-   Peking University Informatics Winter Experience Camp (PKUWC): held around the time of the Winter Camp.
-   Peking University Informatics Experience Camp (PKUSC): usually held on campus in June. Since the contest takes place in the university's computer labs, the environment is Windows and the contest system is OpenJudge.
-   Peking University Summer School for Secondary-School Students (Informatics): held during the summer holidays for science-track students in the second year of senior high school.

#### Tsinghua University (THU)

-   The Department of Computer Science's "secondary-to-university bridging" winter seminar and teaching event: equivalent to an informatics winter camp, sometimes abbreviated in English as THUWC. It usually lasts two days, with contests in the morning (a standard OI contest on the first day and Tsinghua's own "engineering problem" contest on the second day) and course training in the afternoon.

## OI contests in other countries and regions

### USA: USACO

Official website: <http://www.usaco.org/>

USACO is perhaps the foreign OI contest most familiar to Chinese contestants (and probably also the foreign OI contest with the most Chinese-language editorials).

Every year from winter to early spring, USACO holds one online contest per month. A contest lasts 3–5 hours.

According to the official website, USACO contests are divided into these 4 difficulty divisions (3 before the 2015–2016 season):

-   the Bronze division, suitable for programming beginners, especially students who have only learned the most basic algorithms (e.g. sorting, binary search);
-   the Silver division, suitable for students starting to learn basic algorithmic techniques (e.g. recursion, search, greedy algorithms) and basic data structures;
-   the Gold division, where students encounter more complex algorithms (e.g. shortest paths, DP) and more advanced data structures;
-   the Platinum division, suitable for contestants with solid algorithm-design skills; the Platinum division helps them challenge themselves with complex and more open-ended problems.

In China, the OJ platform with the most complete collection of USACO problems is currently Luogu.

### Poland: POI

Official website: <https://oi.edu.pl/>

Official submission site: <https://szkopul.edu.pl/p/default/problemset/>

POI is the foreign OI contest most frequently practiced by many provincial-selection contestants.

According to the description on the [POI official website](https://oi.edu.pl/l/42/), POI proceeds as follows:

-   first round: six problems (five up to and including the 31st edition), online contest;
-   second round: one trial contest and two official contests, where the trial contest has one problem and each official contest has two;
-   third round: one trial contest and two official contests, where the trial contest has one problem and each official contest has three.

In some years, a contest named ONTAK was held, officially called the POI training camp, comparable to China's national training team camp (CTT).

In addition, Poland also holds an open contest called PA, roughly "Algorithmic Battles", whose official website is <https://potyczki.mimuw.edu.pl/>.

Among Chinese OJs, the one with the most complete collection of POI problems is currently BZOJ.

### Croatia: COCI

Official website (English): <http://www.hsin.hr/coci/>

Official website (Croatian): <http://www.hsin.hr/honi/>

A contest with a very wide difficulty range, roughly from popularization-minus to provincial-selection-minus.

In the past, COCI provided problem statements, data, editorials and reference solutions for all problems. From the end of 2017, COCI's editorials and reference solutions stopped being updated. In the 2019–2020 season, editorials and reference solutions resumed.

Luogu, BZOJ and LibreOJ all have a small number of COCI problems.

### Japan: JOI

Official website: <https://www.ioi-jp.org/>

JOI (Japanese: 日本情報オリンピック, the Japanese Olympiad in Informatics) provides problem statements, data, editorials and reference solutions for all problems. In the last couple of years the JOI Final and the Spring Camp have provided English statements, but no English editorials. JOI Open has provided English statements and editorials every year.

The JOI process:

-   preliminary round (予選)
-   final round (本選/JOI Final)
-   spring camp (春季トレーニング合宿/JOI Spring Camp/JOISC)
-   open contest (通信教育/JOI Open Contest)

The preliminary round is relatively easy and, since the 2019/2020 season, consists of several rounds. The difficulty of the JOI Final ranges roughly from advanced-minus to advanced-plus. The difficulty of JOISC and JOI Open problems ranges from advanced to NOI-minus.

The vast majority of JOI problems can be submitted on [AtCoder](https://atcoder.jp/). You can find more JOI problems (Japanese statements) on the JOI official website or on AtCoder.

LibreOJ and BZOJ currently have the JOI Final, JOISC and JOI Open problems of recent years.

### Russia: ROI

Official website: <http://neerc.ifmo.ru/school/archive/index.html>

Online submission: <https://contest.yandex.ru/roiarchive/> and Codeforces (partially).

ROI (Russian: олимпиадная информатика, the Russian Olympiad in Informatics) is Russia's informatics competition.

Process:

-   municipal stage (Municipal Stage/Муниципальный этап)
-   regional stage (Regional Stage/Региональный этап)
-   final stage (Final Stage/Заключительный этап)

LibreOJ currently has translations of the ROI final-stage problems of recent years.

In addition, other large Russian contests for secondary-school students include:

-   the Internet Olympiads in Informatics (Russian: Интернет-олимпиады по информатике)
    -   official website: <http://neerc.ifmo.ru/school/io/index.html>
    -   this contest is organized by the ROI problem setters.
-   the All-Russian Team Olympiad for School Students (Russian: Всероссийской командной олимпиады школьников)
    -   official website: <http://neerc.ifmo.ru/school/russia-team/index.html>
    -   its qualifying contest, the Moscow Team Olympiad, can be submitted on Codeforces.
-   Innopolis Open
    -   official website: <https://olymp.innopolis.ru/en/ooui/information/>
-   the Open Olympiad in Programming for School Students (Открытая олимпиада школьников по программированию)
    -   official website: <https://olympiads.ru/zaoch/>
    -   the official website states that this contest is comparable to ROI.

### Canada: CCC & CCO

CCC (Canadian Computing Competition) and CCO (Canadian Computing Olympiad); information and problems of past editions can be found on the [official website](https://cemc.math.uwaterloo.ca/contests/past_contests.html#ccc).

[CCC](https://dmoj.ca/problems/?category=4) and [CCO](https://dmoj.ca/problems/?category=24) problems can be submitted on DMOJ, which also has CCC editorials.

CCC Junior/Senior is close to the difficulty of the NOIP popularization/advanced group. Winning a gold medal at CCO probably requires the level of an NOI silver medal.

### Singapore: NOI SG

Official website: <https://noisg.comp.nus.edu.sg/noi/>

Its full name is the Singapore National Olympiad in Informatics, also referred to as NOI in the Singaporean context when no ambiguity arises. In format it is divided into the Online Qualification Contest and the Final Contest. Schools register for the online qualification contest as units; contestants compete at their own school and submit remotely over the internet. Qualification results are ranked only within the school, and the top 5 contestants with nonzero scores qualify to represent the school at the national final.

Chinese OJs currently have very few NOI SG problems; statements, test data and official reference programs of past years can be found on the [official GitHub account](https://github.com/noisg).

### Taiwan: Informatics Olympiad (資訊奧林匹亞競賽)

Taiwan translates the "informatics" in OI as "資訊" rather than the translation "信息" commonly used in mainland China.

Contestants from Taiwan who want to participate in IOI have to go through the following rounds:

-   the regional informatics competition (區域資訊學科能力競賽)
-   the national informatics competition (全國資訊學科能力競賽)
-   the informatics training camp (資訊研習營, TOI)

### Other countries

-   Australia: AIO: <https://orac.amt.edu.au/hub/aio/>

    -   difficulty similar to NOI.

-   United Kingdom: British Informatics Olympiad: <https://www.olympiad.org.uk/>

    -   the difficulty is too low.

-   Czech Republic: Matematická olympiáda–kategorie P: <http://mo.mff.cuni.cz/p/archiv.html>

-   Romania: Olimpiada Nationala de Informatica: <http://olimpiada.info/>
    -   look for statements, test data and editorials in the tabs labeled Subiecte.

## Other international OI contests

### BalticOI

**BalticOI** is aimed at the countries around the Baltic Sea. BalticOI 2018 had 9 participating countries, including Lithuania, Poland, Estonia and Finland. The problems are hard.

Except for 2017, BalticOI publishes statements, test data and editorials every year. BalticOI has no fixed official website; each year's host creates a new site. See the [post](https://loj.ac/article/416) for the official websites of past years.

LibreOJ currently has the BalticOI problems of the last ten or so years.

### BalkanOI

**BalkanOI** is aimed at the countries of the Balkan region. BalkanOI 2018 had 12 participating countries, including Romania, Greece, Bulgaria and Serbia. The problems are hard.

BalkanOI has published statements, test data and editorials only in certain years; see the [post](https://loj.ac/article/416) for the official websites.

### CEOI

The participating countries of CEOI 2018 partly overlap with the two contests above and include Poland, Romania, Georgia, Croatia and others. The problems are hard.

CEOI publishes statements, test data and editorials every year; see the [post](https://loj.ac/article/416) for the official websites.

### eJOI

**eJOI** stands for the European Junior Olympiad in Informatics. Participating countries include Russia, Armenia, Bulgaria, Poland and others. The problems are fairly hard.

eJOI publishes statements, test data and editorials every year; see the [post](https://loj.ac/article/416) for the official websites.

### NOI

???+ warning "Warning"
    This is not the Chinese National Olympiad in Informatics.

**NOI** stands for the Nordic Olympiads in Informatics.

Official website: <http://nordic.progolymp.se>

A contest that only started in the last couple of years, aimed at the Nordic countries.

## References

-   [ICPC/CCPC contests and contest formats](./icpc.md)
-   ["Translation group" – websites of some continental OI contests](https://loj.ac/article/416)
