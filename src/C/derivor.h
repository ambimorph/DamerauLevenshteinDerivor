#include "Judy.h"
#include "zstr.h"

const static size_t DERIVORMAXWORDSIZE=64;

/**
 * Prints variations to stdout, space-separated, '\n' terminated.  Also calls fflush(stdout).
 */
void
derive(czstr cz, const Pvoid_t* UP);

/**
 * Prints variations which have the same capitalization style to stdout, space-separated, '\n' terminated.  Also calls fflush(stdout).
 * There are four capitalization styles: "alllower", "ALLUPPER", "Capitalized", and "AnytHINgElse".  derive_with_cap() if the argument falls into one of the first three categories then derive_with_cap() will return only words that are in that category themselves.  If the argument is in the fourth category then derive_with_cap() will do the same thing as derive() does (namely, try lots of capitalization variants and return any that are in the vocabulary UP).
 */
void
derive_with_cap(czstr cz, const Pvoid_t* UP);

