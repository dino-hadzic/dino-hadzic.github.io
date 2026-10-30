---
title: Radians and coordinate systems
---

## Definition of an angle

In elementary or middle school we learned the **static definition** of an angle: an angle is the figure formed by two rays with a common endpoint.

However, this definition restricts angles to $[0, 360^\circ]$, which makes deeper study harder, and some things cannot be explained with it, e.g.: what does a rotation by $720^\circ$ mean?

High-school mathematics introduces the **dynamic definition** of an angle: an angle is the figure formed by rotating a ray in the plane around its endpoint from one position to another.

The starting position is called the **initial side**, and the ending position the **terminal side**. By convention:

-   an angle formed by rotating **counterclockwise** is called a **positive angle**, and its measure is positive;
-   an angle formed by rotating **clockwise** is called a **negative angle**, and its measure is negative;
-   an angle whose terminal side has not been rotated at all relative to the initial side is called the **zero angle**, and its measure is $0^\circ$.

This extends the concept of an angle to **arbitrary angles**.

???+ note "Note"
    The initial and terminal sides of the zero angle coincide, but not every angle whose initial and terminal sides coincide is the zero angle, e.g. angles that are multiples of $360^\circ$.

## Radian measure

In practical applications angles often have to be converted into various other parameters, and describing angles in radians reduces the number of coefficients needed. So next we introduce **radian measure**:

The central angle subtended by an arc whose length equals the radius is called an angle of $1$ radian; it is denoted by the symbol $\text{rad}$ and read "radian".

By the convention above, the radian measure of a positive angle is positive, that of a negative angle is negative, and that of the zero angle is $0$. If a central angle $\alpha$ of a circle of radius $r$ subtends an arc of length $l$, then:

$$
|\alpha|=\dfrac{l}{r}
$$

Using this formula one can also write down the formulas for arc length and sector area, which we skip here.

Thus a $360^\circ$ angle has radian measure $2\pi$; with this correspondence we can convert between degrees and radians:

$$
k \operatorname{rad} = \frac{\pi}{180^\circ} n^\circ
$$

Consider an angle and rotate its terminal side by one more full turn, or even several turns, while the initial side stays in place; the position of the terminal side is always the same. We call such angles angles with the same terminal side.

The set of angles with the same terminal side as the angle $\alpha$ is easy to obtain: it is $\{\varphi \mid \varphi = \alpha + 2k\pi, k \in \mathbf{Z}\}$.

It can be understood as follows: we keep adding full turns to the side of the angle, and the position of the terminal side does not change.

???+ note "The two mathematical constants $\pi$ and $\tau$"
    Some people in the Western mathematical community today hold that the "true circle constant" should be $2\pi$, and denote this value by the Greek letter $\tau$. Supporters of the new circle constant celebrate the "true" Pi Day on June 28.
    
    For example, in radian measure a full angle is $2\pi$, so dividing $2\pi$ into equal parts directly gives equal parts of the full angle. Also, the combination $2\pi$ appears very frequently in complex analysis, and so on.
    
    To follow the convention established throughout China, **OI Wiki** uses $\pi$ for the circle constant.

???+ note "Customary way of writing pi in programming"
    In C/C++, $\pi$ is usually taken as `acos(-1)`; only this value is the floating-point number closest to $\pi$. The $\pi$ written using `acos(-1)` or `4 * atan(1)` is $3.14159265358979310000$.
    
    If other values are used, e.g. `acos(-1.0/2.0)`, `acos(1.0/2.0)`, `asin(1.0/2.0)`, etc., the resulting $\pi$ is $3.14159265358979360000$, which is no longer the floating-point number closest to $\pi$.
    
    If you can memorize it, you may also directly write $3.1415926535897932$.

## Rectangular coordinate system in the plane

Two mutually perpendicular number axes in the same plane with a common origin form a rectangular (Cartesian) coordinate system in the plane (rectangular coordinates).

Usually one axis is placed horizontally and the other vertically, and the directions to the right and upward are taken as the positive directions of the two axes. The horizontal axis is called the $x$-axis or the axis of abscissas, the vertical axis is called the $y$-axis or the axis of ordinates; the $x$-axis and the $y$-axis together are called the coordinate axes, and their common origin $O$ is called the origin of the rectangular coordinate system. The rectangular coordinate system with origin $O$ is denoted by $xOy$.

The $x$-axis and the $y$-axis divide the coordinate plane into four quadrants: the upper right part is called the first quadrant, and the other three parts, in counterclockwise order, are called the second, third and fourth quadrants. The quadrants are bounded by the axes; points on the horizontal and vertical axes and the origin do not belong to any quadrant. In general, the $x$-axis and the $y$-axis use the same unit length, but in special cases different unit lengths may be used.

### Describing positions in the rectangular coordinate system

In the rectangular coordinate system, every point of the plane corresponds to a unique ordered pair of numbers (the coordinates of the point); conversely, every ordered pair of numbers corresponds to a unique point of the plane.

For an arbitrary point $C$ of the plane, drop perpendiculars from $C$ to the $x$-axis and to the $y$-axis; the numbers $a, b$ corresponding to the feet of the perpendiculars on the $x$-axis and the $y$-axis are called the abscissa and the ordinate of the point $C$, respectively, and the ordered pair $(a, b)$ is called the rectangular coordinates of the point $C$. Points in different quadrants or on the coordinate axes have different coordinates.

## Polar coordinate system in the plane

Consider a real-life situation, such as navigation at sea: one says "point $B$ is in the direction $30^\circ$ east of north from point $A$, at a distance of $100$ meters", rather than "set up a rectangular coordinate system with origin $A$; then $B(50,50\sqrt 3)$".

So:

1.  choose a fixed point $O$ in the plane, called the **pole**;
2.  draw a ray $Ox$ from the pole, called the **polar axis**;
3.  choose a unit length (usually $1$ in mathematical problems), a unit of angle (usually the radian) and its positive direction (usually counterclockwise);

and the **polar coordinate system** is established.

### Describing positions in the polar coordinate system

Let $A$ be a point of the plane.

-   The distance $|OA|$ between the pole $O$ and $A$ is called the **polar radius**, denoted by $\rho$;
-   the angle $\angle xOA$ with the polar axis as initial side and $OA$ as terminal side is called the **polar angle**, denoted by $\varphi$;

then the ordered pair $(\rho,\varphi)$ is the **polar coordinates** of $A$.

By the definition of angles with the same terminal side, $(\rho,\varphi)$ and $(\rho,\varphi + 2k\pi)\ (k\in \mathbf{Z})$ actually represent the same point. In particular, the polar coordinates of the pole are $(0,\varphi)\ (\varphi \in \mathbf{R})$, so a point of the plane has infinitely many polar coordinate representations.

If we require $\rho \ge 0,0 \le \varphi < 2\pi$, then every point of the plane other than the pole can be represented by a unique ordered pair $(\rho,\varphi)$, and the point represented by the polar coordinates $(\rho,\varphi)$ is uniquely determined.

### Conversion between rectangular and polar coordinates

Of course, studying figures in the polar coordinate system is sometimes inconvenient. To switch to the rectangular coordinate system there are conversion formulas. The rectangular coordinates $(x,y)$ of the point $A(\rho,\varphi)$ can be expressed as follows:

$$
\begin{aligned}
x &= \rho \cos \varphi \\
y &= \rho \sin \varphi
\end{aligned}
$$

Hence:

$$
\begin{aligned}
\rho^2 &= x^2 + y^2\\
\tan \varphi &= \frac{y}{x}\ \ \ \ (x\not =0)
\end{aligned}
$$

So $\rho = \sqrt{x^2+y^2}$.

However, for the same $\dfrac{y}{x}$, i.e. the same $\tan\varphi$, there are two possible values of $\varphi$, so the direction must additionally be determined from the values of $x, y$. Specifically, define the function:

$$
\operatorname{atan2}(y, x) = \begin{cases}
\arctan(\frac{y}{x}) & \text{if } x > 0 \\
\arctan(\frac{y}{x}) + \pi & \text{if } y \ge 0, x < 0 \\
\arctan(\frac{y}{x}) - \pi & \text{if } y < 0, x < 0 \\
\pi/2 & \text{if } y > 0, x = 0 \\
-\pi/2 & \text{if } y < 0, x = 0 \\
\text{any} & \text{if } y = 0, x = 0
\end{cases}
$$

Then $\varphi = \operatorname{atan2}(y, x)$. Note that the range of this function is $(-\pi, \pi]$.

In C/C++, [this function](https://en.cppreference.com/w/cpp/numeric/math/atan2) is defined in the `<math.h>` or `<cmath>` library; just call `atan2(y, x)`.

## Rectangular coordinate system in space

A rectangular coordinate system in space is established as follows:

1.  choose a point $O$ in space;
2.  through $O$ draw three mutually perpendicular number axes $\overrightarrow{Ox}, \overrightarrow{Oy}, \overrightarrow{Oz}$, called the $x$-axis (axis of abscissas), the $y$-axis (axis of ordinates) and the $z$-axis (vertical axis), respectively, and together the coordinate axes; their positive directions follow the right-hand rule: if the right hand grips the $z$-axis so that its four fingers curl from the positive direction of the $x$-axis toward the positive direction of the $y$-axis, the thumb points in the positive direction of the $z$-axis;
3.  set the unit length on each axis, usually $1$.

This forms a rectangular coordinate system in space, denoted by $O-xyz$. The fixed point $O$ is called the origin of the coordinate system.

Any two coordinate axes determine a plane, so three mutually perpendicular planes are determined, together called the coordinate planes. The coordinate plane determined by the $x$-axis and the $y$-axis is called the $xOy$-plane, and similarly there are the $yOz$-plane and the $zOx$-plane. The three coordinate planes divide space into eight parts, each of which is called an octant.

### Describing positions in the rectangular coordinate system in space

Once a rectangular coordinate system $O-xyz$ in space is fixed, a one-to-one correspondence between points of space and ordered triples can be established.

Let $M$ be a point of space, and through $M$ draw planes perpendicular to the $x$-axis, the $y$-axis and the $z$-axis, respectively. Let the intersections of the three planes with the $x$-axis, the $y$-axis and the $z$-axis be $P, Q, R$, respectively; the points $P, Q, R$ are called the projections of $M$ onto the $x$-axis, the $y$-axis and the $z$-axis. Let the coordinates of $P, Q, R$ on the $x$-axis, the $y$-axis and the $z$-axis be $x, y, z$, respectively; thus the point $M$ determines an ordered triple $(x, y, z)$.

Conversely, given an ordered triple $(x, y, z)$, take the point $P$ with coordinate $x$ on the $x$-axis, the point $Q$ with coordinate $y$ on the $y$-axis and the point $R$ with coordinate $z$ on the $z$-axis, then through $P, Q, R$ draw three planes perpendicular to the $x$-axis, the $y$-axis and the $z$-axis, respectively. They intersect in a single point $M$ of space, and $M$ is the point determined by the ordered triple $(x, y, z)$.

In this way a one-to-one correspondence is established between points $M$ of space and ordered triples $(x, y, z)$. The ordered triple $(x, y, z)$ is called the coordinates of the point $M$, written $M(x, y, z)$, where $x$ is called the abscissa, $y$ the ordinate and $z$ the applicate (the vertical coordinate).

## Cylindrical coordinate system

The cylindrical coordinate system extends polar coordinates to three dimensions: start from the polar coordinate system used for work in the plane, then add a $z$-axis through the pole $O$ perpendicular to that plane, pointing upward.

To find the point described by the cylindrical coordinates $(\rho, \varphi, z)$, first handle $\rho$ and $\varphi$ in the polar coordinate system, then move "up" or "down" along the $z$-axis according to the $z$ coordinate.

### Conversion between cylindrical and rectangular coordinates in space

The value of $z$ is the same in both systems.

For the conversion between $(x,y)$ and $(\rho, \varphi)$ see [Conversion between rectangular and polar coordinates](#conversion-between-rectangular-and-polar-coordinates) above.

## Spherical coordinate system

Spherical coordinates can be determined as follows:

1.  stand at the origin, facing the direction of the horizontal polar axis; the vertical axis points from the feet to the head;
2.  raise the arm upward, pointing in the direction of the vertical polar axis;
3.  rotate counterclockwise by the angle $\varphi$;
4.  lower the arm by the angle $\vartheta$; the arm now points in the direction specified by $\varphi$ and $\vartheta$;
5.  move from the origin in that direction by the distance $r$.

This reaches the point described by the spherical coordinates $(r,\vartheta,\varphi)$. Here $\vartheta$ is called the **zenith angle** and $\varphi$ the **azimuthal angle**.

???+ warning "Warning"
    For various reasons, some sources use $\phi$ for the zenith angle and $\theta$ for the azimuthal angle. When you encounter spherical coordinate systems in articles, be sure to pay attention to this.
    
    Likewise, when writing an article that uses spherical coordinates, it is recommended to state clearly in advance which symbols denote the zenith and azimuthal angles.

### Conversion between cylindrical and spherical coordinates

The value of $\varphi$ is the same in both systems.

From cylindrical to spherical coordinates:

$$
\begin{aligned}
r &= \sqrt{\rho^2 + z^2} \\
\vartheta &= \begin{cases}
\arctan\left(\frac{\rho}{z}\right) & \text{if }z > 0 \\
\pi/2 & \text{if }z = 0, \rho \not= 0 \\
\arctan\left(\frac{\rho}{z}\right) + \pi & \text{if }z < 0 \\
\end{cases}
\end{aligned}
$$

Note that for the point $(0,0,0)$ in cylindrical coordinates, the spherical coordinate $\vartheta$ is undefined.

From spherical to cylindrical coordinates:

$$
\begin{aligned}
\rho &= r \sin \vartheta \\
z &= r \cos \vartheta
\end{aligned}
$$

### Conversion between rectangular coordinates in space and spherical coordinates

One can combine [Conversion between rectangular and polar coordinates](#conversion-between-rectangular-and-polar-coordinates) and [Conversion between cylindrical and spherical coordinates](#conversion-between-cylindrical-and-spherical-coordinates) above, or use the following formulas directly:

From rectangular coordinates in space to spherical coordinates:

$$
\begin{aligned}
r &= \sqrt{x^2 + y^2 + z^2} \\
\vartheta &= \arccos\left(\frac{z}{\sqrt{x^2 + y^2 + z^2}}\right) \\
\varphi &= \operatorname{atan2}(y, x)
\end{aligned}
$$

where the definition of $\operatorname{atan2}$ is given in [Conversion between rectangular and polar coordinates](#conversion-between-rectangular-and-polar-coordinates).

Note that for the point $(0,0,0)$ in rectangular coordinates in space, the spherical coordinates $\vartheta$ and $\varphi$ are undefined.

From spherical coordinates to rectangular coordinates in space:

$$
\begin{aligned}
x &= r \sin \vartheta \cos \varphi \\
y &= r \sin \vartheta \sin \varphi \\
z &= r \cos \vartheta
\end{aligned}
$$
