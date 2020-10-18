#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "methods.h"

/**
 * Gets an exact solution of u function
 *
 * @param x an x value
 * @return a calculated value
 */
extern double getExactlySolution(double x);

/**
 * Gets a numeric solution of u' function
 *
 * @param x an x value
 * @param u an u value
 *
 * @return a calculated value
 */
extern double getNumericSolution(double x, double u);

/**
 * Entry point
 *
 * @return a program status code (0 if successful)
 */
int main() {
    double xStart = 0.0;
    double xEnd = 1.0;

    int stepsCount = 100;
    double stepLength = (xEnd - xStart) / stepsCount;

    double xCurrent = xStart;
    double xNext = xCurrent + stepLength;

    double exactlySolution = getExactlySolution(xStart);
    double numericSolutionByRugneKutta = xStart;
    double numericSolutionByEuler = xStart;

    printf("%s\t\t%s\t%s\t%s\t\t%s\n", "Exactly", "Numeric E", "Numeric RK", "Error E", "Error RK");

    const char* messageFormat = "%lf\t%lf\t%lf\t%lf\t%lf\n";
    for (int i = 0; i < stepsCount; i++) {
        double eulerError = fabs(exactlySolution - numericSolutionByEuler);
        double rugneKuttaError = fabs(exactlySolution - numericSolutionByRugneKutta);

        printf(
            messageFormat,
            exactlySolution,
            numericSolutionByEuler,
            numericSolutionByRugneKutta,
            eulerError,
            rugneKuttaError
        );

        xCurrent += stepLength;
        xNext += stepLength;

        exactlySolution = getExactlySolution(xNext);

        numericSolutionByEuler = getNextValueByEulerMethod(
                getNumericSolution,
                xNext,
                numericSolutionByEuler,
                stepLength
        );

        numericSolutionByRugneKutta = getNextValueByRugneKuttaMethod(
            getNumericSolution,
            xCurrent,
            numericSolutionByRugneKutta,
            stepLength
        );
    }

    return 0;
}

/**
 * {@inheritDoc}
 */
double getExactlySolution(double x) {
    return pow(x, 4);
}

/**
 * {@inheritDoc}
 */
double getNumericSolution(double x, double u) {
    if (0 == x) {
        printf("Cannot be divided by zero");
        exit(EXIT_FAILURE);
    }

    return (2 * pow(x, 4) + 2 * u) / x;
}
