/** {modelname!u}_SDE.h
 *
 * {modelname!u} - Stochastic Differential Equations
 *
 * Author: {user}
 * {date}
 */

#ifndef {modelname!u}_SDE_H
#define {modelname!u}_SDE_H
#include <assist/methods/sim_history.h>
#include <assist/models/model_sde.h>

class {modelname}SDE: public ModelSDE {{
private:
    VECTOR integrated;
public:
    /* sde_model inheritance:
        const int dim;    // Phase space dimension
        VECTOR x0;        // Initial population
        VECTOR drift;     // Same dimension as phase space
        MATRIX diffusion; // Diffusion matrix */
    // @begin-properties
    // @end-properties
    {modelname}SDE():
        ModelSDE("{modelname}SDE", {dim}),
        integrated({dim})
    {{
        {x0}
        trace("{modelname}SDE(dim:{dim}) executed.\n");
    }}
    void compute_dd(const VECTOR& sm,
                    double dt,
                    const sim_history& hist,
                    const VECTOR& kernel)
    {{
        trace("{modelname}SDE.compute_dd() executed.\n");
    }}
}};

#endif
