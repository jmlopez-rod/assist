/** {modelname!u}_SSA.h
 *
 * {modelname!u} - Stochastic Simulation Algorithm
 *
 * Author: {user}
 * {date}
 */

#ifndef {modelname!u}_SSA_H
#define {modelname!u}_SSA_H
#include <assist/models/model_ssa.h>

class {modelname}SSA: public ModelSSA {{
public:
    /* ModelSSA inheritance:
        const char* name;
        const int num_specs, num_reacs;
        VECTOR x0, prop;
        MATRIX_INT z; */
    // @begin-properties
    // @end-properties
    {modelname}SSA():
        ModelSSA("{modelname}SSA", {nspecs}, {nreacs})
    {{
        {x0}
        // The element z(s, r) denotes the change
        // to the species s due to the reaction r
        {z}
        trace("{modelname}SSA() executed.\n");
    }}
    void eval_prop(const VECTOR& sm) {{
        {prop}
    }}
}};

#endif
