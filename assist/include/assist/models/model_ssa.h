/** MODEL_SSA.H
 * Manuel Lopez - jmlopez@math.uh.edu
 * Department of Mathematics,
 * University of Houston.
 * May 19, 2013 - Agust 2, 2014
 */

#ifndef MODEL_SSA_H
#define MODEL_SSA_H

class ModelSSA {
public:
    // @begin-properties
    const char* name;
    const int num_specs;
    const int num_reacs;
    VECTOR x0;
    VECTOR prop;
    MATRIX_INT z;
    // @end-properties
    ModelSSA(const char* name_, int ns_, int nr_):
        name(name_),
        num_specs(ns_),
        num_reacs(nr_),
        x0(ns_),
        prop(nr_),
        z(ns_, nr_)
    {
        trace("ModelSSA('%s', NS:%d, NR:%d) executed.\n", name_, ns_, nr_);
    }
};

#endif
