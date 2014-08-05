.. _make-collector:

*************************
Creating a Data Collector
*************************

To create a new method you can use the ``mkcollector`` command

.. code-block:: sh

    assist collector NewTimeSeries

This will produce a template so that you may define the necessary
definitions for the functions used during a simulation.

.. code-block:: cpp

    /** NEWTIMESERIES.h
     *
     * Author: jmlopez
     * Mon Aug 04, 2014 11:37:05 PM
     */

    #ifndef NEWTIMESERIES_H
    #define NEWTIMESERIES_H

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
    */
    class NewTimeSeries {
    private:
        bool complete;
        BaseMethod& sm;
        /* BaseMethod properties:
            const char* name;
            double time, time_step;
            VECTOR x, x_prev; */
    public:
        NewTimeSeries(BaseMethod& sm_): sm(sm_), complete(false) {
            // Initialize your collector here
            trace("NewTimeSeries(METHOD:%s) executed.\n", sm.name);
        }
        void new_trial() {
            // Reset variables if more than one trial is executed.
            trace("NewTimeSeries.new_trial() executed.\n");
        }
        bool process_info() {
            // This function should be called after the simulation
            // method has updated the system.
            trace("NewTimeSeries.process_info() executed.\n");
            return false;
        }
        void end_trial() {
            // Is there anything that needs to be done once the trial is
            // done?
            trace("NewTimeSeries.end_trial() executed.\n");
        }
        void end_sim() {
            // There might be code to write after the simulation is
            // completed. Write it here
            trace("NewTimeSeries.end_sim() executed.\n");
        }
        bool is_complete() const {
            trace("NewTimeSeries.complete() executed: %s\n", 
                  (complete ? "true": "false"));
            return complete;
        }
    };

    #endif

We may now proceed to specify the specific characteristics of the
data collector.
