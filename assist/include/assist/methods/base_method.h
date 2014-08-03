/** BASE_METHOD.H
 * Manuel Lopez - jmlopez@math.uh.edu
 * Department of Mathematics, 
 * University of Houston.
 * July 24, 2013
 */

#ifndef BASE_METHOD_H
#define BASE_METHOD_H

class BaseMethod {
public:
    // @begin-properties
    const char* name;
    double time, time_step;
    VECTOR x;
    VECTOR x_prev;
    // @end-properties
    BaseMethod(const char* n_, int dim_):
        name(n_),
        x(dim_),
        x_prev(dim_)
    {
        trace("BaseMethod('%s', '%d') executed.\n", name, dim_);
    }
};

#endif
