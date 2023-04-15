#!/usr/bin/env python3

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#
# Try:

#  -  Minimize the number of invocations of the print() function by inserting the sequence \n in the strings.

print("    *",
      "   * *",
      "  *   *",
      " *     *",
      "***   ***",
      "  *   *",
      "  *   *",
      "  *****",
      sep='\n')

#  -  Make the arrow twice as big (while maintaining proportions).

print("      *",
      "     * *",
      "    *   *",
      "   *     *",
      "  *       *",
      " *         *",
      "***       ***",
      "  *       *",
      "  *       *",
      "  *       *",
      "  *       *",
      "  *********",
      sep='\n')

#  -  Duplicate the arrow by placing both arrows side by side

print("      *       " * 2,
      "     * *      " * 2,
      "    *   *     " * 2,
      "   *     *    " * 2,
      "  *       *   " * 2,
      " *         *  " * 2,
      "***       *** " * 2,
      "  *       *   " * 2,
      "  *       *   " * 2,
      "  *       *   " * 2,
      "  *       *   " * 2,
      "  *********   " * 2,
      sep='\n')
