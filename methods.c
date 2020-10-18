#include "methods.h"

/**
 * {@inheritDoc}
 */
double getNextValueByRugneKuttaMethod(double (*f) (), double x, double u, double h) {
    double F1 = h * f(x, u);
    double F2 = h * f(x + h / 2, u + F1 / 2);
    double F3 = h * f(x + h / 2, u + F2 / 2);
    double F4 = h * f(x + h, u + F3);

    return u + (F1 + 2 * F2 + 2 * F3 + F4) / 6;
}

/**
 * {@inheritDoc}
 */
double getNextValueByEulerMethod(double (*f) (), double x, double u, double h) {
    return u + h * f(x);
}
