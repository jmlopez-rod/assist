/** MODEL_SDE.H
 * Manuel Lopez - jmlopez@math.uh.edu
 * Chinmaya Gupta - chinmaya@math.uh.edu
 * Department of Mathematics,
 * University of Houston.
 * July 24, 2013 - August 3, 2014
 */

#ifndef MODEL_SDE_H
#define MODEL_SDE_H

class ModelSDE {
public:
    // @begin-properties
    const char* name;
    const int dim;    // Phase space dimension
    VECTOR x0;        // Initial population
    VECTOR drift;     // Same dimension as phase space
    MATRIX diffusion; // Diffusion matrix
    // @end-properties
    ModelSDE(const char* name_, int dim_):
        name(name_),
        dim(dim_),
        x0(dim_),
        drift(dim_),
        diffusion(dim_, dim_)
    {
        trace("ModelSDE(DIM:%d) executed.\n", dim_);
    }
};

#endif
