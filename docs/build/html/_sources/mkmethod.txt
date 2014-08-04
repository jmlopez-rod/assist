.. _make-method:

*****************
Creating a Method
*****************

To create a new method you can use the ``mkmethod`` command

.. code-block:: sh

    assist mkmethod NewGillespie ssa

This will produce a template so that you may define the necessary
definitions for the functions used during a simulation.

.. code-block:: cpp

    /** NEWGILLESPIE.h
     *
     * Author: jmlopez
     * Sun Aug 03, 2014 07:50:27 PM
     */

    #ifndef NEWGILLESPIE_H
    #define NEWGILLESPIE_H
    #include <assist/methods/base_method.h>

    /* EXCENTURY REFERENCE:
      VECTOR x methods:
        x.dim() <==> x.size(): Number of elements
        x[n] <==> x(n): access the nth entry
      MATRIX x methods:
        x.dim(0) <==> Number of rows
        x.dim(1) <==> Number of columns
        x(r, c) <==> x[r+c*x.dim(0)]
        x.size(0) <==> x.dim(0)
        x.size(1) <==> x.dim(0)*x.dim(2)
      MTRand rg methods:
        rg.randInt(): Integer in [0, 2^32-1]
        rg.rand(): Real in (0,1)
        rg.randInc(): Real in [0,1]
        rg.randIL(): Real in [0,1)
        rg.normal(m,s): From normal distribution
        rg.gamrnd(a,b): From gamma distribution
    */

    class NewGillespie: public BaseMethod {
    public:
        /* BaseMethod inheritance:
            const char* name;
            double time, time_step;
            VECTOR x, x_prev; */
        // @begin-properties
        ModelSSA& model;
        MTRand rg; // A random number generator
        // @end-properties
        NewGillespie(ModelSSA& m_):
            BaseMethod("NewGillespie", m_.num_specs),
            rg(),
            model(m_)
        {
            trace("NewGillespie('%s') executed.\n", m_.name);
        }
        void new_trial() {
            time = 0.0;
            time_step = 0.0;
            for (int i = 0; i < model.num_specs; ++i) {
                x[i] = x_prev[i] = model.x0[i];
            }
            // Insert more code if needed.
            trace("NewGillespie.new_trial() executed.\n");
        }
        void get_time_step() {
            // Calculate how to obtain time_step
            trace("NewGillespie.get_time_step(): time_step <- %lf\n", time_step);
        }
        bool update_system() {
            // Update the system under the assumption that time_step has
            // been calculated.
        }
        void end_trial() {
            // In case there is a need to perform something once
            // the trial is finished.
            trace("NewGillespie.end_trial() executed.\n");
        }
    };

    #endif

We may now proceed to specify the specific characteristics of the
method.
