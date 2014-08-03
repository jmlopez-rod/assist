.. _make-model:

****************
Creating a Model
****************

Assist currently provides templates to create two types of models:
ssa and sde. 

SSA Model
=========

To create an ssa model you need to provide the number of species as
well as the number of reactions in the model. The next command creates
a template to simulate the Lotka-Volterra model with two species and
four events.

.. code-block:: sh

    assist mkmodel LotkaVolterra ssa --nspecs 2 --nreacs 4 -z row

The extra option ``-z`` creates all the entries of the state change
matrix. The value of ``row`` allows us to specify the changes on the
species due to an event. In this case we can see a row number as the
event number and as we move entry by entry we specify the change in
an species. When ``-z`` is set to ``col`` then each row in the header
file represents an specie. For instance, the command above produces

.. code-block:: cpp

    /** LOTKAVOLTERRA_SSA.h
     *
     * LOTKAVOLTERRA - Stochastic Simulation Algorithm
     *
     * Author: jmlopez
     * Sat Aug 02, 2014 07:45:50 PM
     */

    #ifndef LOTKAVOLTERRA_SSA_H
    #define LOTKAVOLTERRA_SSA_H
    #include <assist/models/model_ssa.h>

    class LotkaVolterraSSA: public ModelSSA {
    public:
        /* ModelSSA inheritance:
            const char* name;
            const int num_specs, num_reacs;
            VECTOR x0, prop;
            MATRIX_INT z; */
        // @begin-properties
        // @end-properties
        LotkaVolterraSSA():
            ModelSSA("LotkaVolterraSSA", 2, 4)
        {
            x0[0] = 0;
            x0[1] = 0;
            // The element z(s, r) denotes the change
            // to the species s due to the reaction r
            for(unsigned int i=0; i < z.size(1); ++i) z[i] = 0;
            z(0, 0) =  0;  z(1, 0) =  0;
            z(0, 1) =  0;  z(1, 1) =  0;
            z(0, 2) =  0;  z(1, 2) =  0;
            z(0, 3) =  0;  z(1, 3) =  0;

            trace("LotkaVolterraSSA() executed.\n");
        }
        void eval_prop(const VECTOR& sm) {
            prop[0] = 0;
            prop[1] = 0;
            prop[2] = 0;
            prop[3] = 0;
        }
    };

    #endif

We may now proceed to specify the specific characteristics of the
model.

