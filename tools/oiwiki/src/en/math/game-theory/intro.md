---
title: Introduction to game theory
---

**Game theory** is a branch of economics that mainly studies the behavior of individuals in competitive or adversarial situations under given rules. Game theory is concerned with the expected and actual behavior of the participants in a game and studies their optimal strategies.

Put simply, game theory mainly studies the following: how the several players taking part in a game choose their strategies.

## Basic concepts

This section briefly introduces some common concepts of game theory.

### Cooperative and noncooperative games

A **cooperative game** is a game in which the participants can form coalitions and cooperate with each other. In such games, noncooperative behavior of an individual is usually punished by some external mechanism. In contrast, no such mechanism exists in a **noncooperative game**, so the participants either cannot form coalitions at all or can only sustain cooperation through credible threats.

Compared with cooperative games, noncooperative games have been studied more systematically and are better understood. All games discussed in this article are noncooperative games.

### Symmetric and asymmetric games

In a **symmetric game**, different participants receive the same payoff for the same action; that is, the payoff depends only on the action itself and not on the identity of the one who takes it. A game that does not satisfy this condition is called an **asymmetric game**.

### Zero-sum and non-zero-sum games

Main page: [Zero-sum games](./zero-sum-game.md)

A **zero-sum game** is a game in which the total payoff of all participants is always zero, no matter how the parties act. The zero-sum games usually discussed involve two participants; then one side's gain is necessarily the other side's loss. In contrast, a **non-zero-sum game** allows several parties to win or lose together; this includes **positive-sum games**, **negative-sum games**, and so on.

### Simultaneous and sequential games

In a **simultaneous game**, all participants make their decisions at the same time, without knowing the others' choices. Rock-paper-scissors is a typical simultaneous game. Such games are often represented by a payoff matrix and usually do not involve the notion of time.

The opposite is a **sequential game**, in which the participants act one after another. Note that a player who moves later must be able to observe at least part of the actions of the players who moved earlier; otherwise the order of moves would be meaningless. Sequential games are usually described by a game tree.

### Perfect and imperfect information games

**Perfect information** means that whenever a participant makes a decision, they know everything that has happened so far, including the initial state of the game. For example, chess and Go are games of perfect information, whereas mahjong and poker are games of imperfect information, since the players cannot see the other players' hands. Perfect information is usually used to describe sequential games; since in a simultaneous game the players cannot know the action the opponent is about to take, simultaneous games are usually not considered games of perfect information.

### Complete and incomplete information games

**Complete information** means that all participants fully know the structure of the game itself (including the decisions available to each party and the final payoffs), and that this information is common knowledge. The opposite is a game of incomplete information, in which some elements of the game (such as the opponent's available decisions or payoff function) are unknown to the participants.

It is worth noting that "complete information" and "perfect information" are two independent concepts, neither of which implies the other. For example, mahjong is a game of complete but imperfect information, since its rules and payoffs are public but the tiles are not visible; on the other hand, some games with hidden goals but fully public actions are games of perfect but incomplete information.

## Combinatorial game theory

In algorithmic competitions, the most common type of game is the **combinatorial game**. The term usually refers to games that are hard to solve because of their huge number of states. Precisely because general combinatorial games are quite complex, combinatorial game theory mainly focuses on the following type: two-player games with alternating moves, perfect information, and no element of chance. Chess, Go, and the like are typical combinatorial games.

### Impartial combinatorial games

Main page: [Impartial combinatorial games](./impartial-game.md)

An **impartial game** is a combinatorial game satisfying the following conditions:

-   in any given state, all participants have exactly the same moves available, which depend only on the current state and not on the identity of the player;
-   the same state of the game cannot be reached more than once, the game ends when a participant cannot move, and the game always ends after finitely many moves and never in a draw.

Impartial games are always symmetric games.

### Partizan combinatorial games

Main page: [Partizan combinatorial games](./partizan-game.md)

The concept opposite to an impartial game is a **partizan game**, in which the moves a participant can make in a given state depend on their identity. Most board games (such as chess, Chinese chess, Go, and Gomoku) are partizan games, since the participants can only move their own pieces.

### Normal and misère games

In combinatorial games, the winner is usually the participant who makes the last move before the game ends. This is called a **normal game**. The opposite is a **misère game**, in which the participant who makes the last move before the game ends is the loser.

Both impartial and partizan combinatorial games can be normal or misère games.

## References

-   [Game theory - Wikipedia](https://en.wikipedia.org/wiki/Game_theory)
-   [Combinatorial game theory - Wikipedia](https://en.wikipedia.org/wiki/Combinatorial_game_theory)
-   [Impartial game - Wikipedia](https://en.wikipedia.org/wiki/Impartial_game)
-   [Misère - Wikipedia](https://en.wikipedia.org/wiki/Mis%C3%A8re)
