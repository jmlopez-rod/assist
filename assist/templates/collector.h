/** {collectorname!u}.h
 *
 * Author: {user}
 * {date}
 */

#ifndef {collectorname!u}_H
#define {collectorname!u}_H

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
class {collectorname} {{
private:
    bool complete;
    BaseMethod& sm;
    /* BaseMethod properties:
        const char* name;
        double time, time_step;
        VECTOR x, x_prev; */
public:
    {collectorname}(BaseMethod& sm_): sm(sm_), complete(false) {{
        // Initialize your collector here
        trace("{collectorname}(METHOD:%s) executed.\n", sm.name);
    }}
    void new_trial() {{
        // Reset variables if more than one trial is executed.
        trace("{collectorname}.new_trial() executed.\n");
    }}
    bool process_info() {{
        // This function should be called after the simulation
        // method has updated the system.
        trace("{collectorname}.process_info() executed.\n");
        return false;
    }}
    void end_trial() {{
        // Is there anything that needs to be done once the trial is
        // done?
        trace("{collectorname}.end_trial() executed.\n");
    }}
    void end_sim() {{
        // There might be code to write after the simulation is
        // completed. Write it here
        trace("{collectorname}.end_sim() executed.\n");
    }}
    bool is_complete() const {{
        trace("{collectorname}.complete() executed: %s\n", 
              (complete ? "true": "false"));
        return complete;
    }}
}};

#endif
