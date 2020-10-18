#ifndef DIFF_EQ_METHODS_H
#define DIFF_EQ_METHODS_H

/**
 * Calculates an approximated next value by
 * Runge-Kutta method and returns it
 *
 * @link https://www.intmath.com/differential-equations/12-runge-kutta-rk4-des.php
 *
 * @param f a function of differential equation
 * @param x an x value
 * @param u an u value
 * @param h a step value
 *
 * @return an approximated next value
 */
extern double getNextValueByRugneKuttaMethod(double (*f) (), double x, double u, double h);

/**
 * Calculates an approximated next value by
 * Euler method and returns it
 *
 * @link https://en.wikipedia.org/wiki/Euler_method
 *
 * @param f a function of differential equation
 * @param x an x value
 * @param u an u value
 * @param h a step value
 *
 * @return an approximated next value
 */
extern double getNextValueByEulerMethod(double (*f) (), double x, double u, double h);

#endif
