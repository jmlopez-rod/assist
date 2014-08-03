/** TIME_SERIES.h
 * jmlopez - jmlopez@math.uh.edu
 * Department of Mathematics,
 * University of Houston.
 * Jan 04, 2014
 */

#ifndef SPP_TIME_SERIES_H
#define SPP_TIME_SERIES_H

/* VECTOR x methods:
     x.dim() <==> x.size(): Number of elements
     x[n] <==> x(n): access the nth entry
   MATRIX x methods:
     x.dim(0) <==> Number of rows
     x.dim(1) <==> Number of columns
     x(r, c) <==> x[r+c*x.dim(0)]
     x.size(0) <==> x.dim(0)
     x.size(1) <==> x.dim(0)*x.dim(2) */
class TimeSeries {
public:
    bool complete;
    BaseMethod& sm;
    /* BaseMethod properties:
        const char* name;
        double time, time_step;
        VECTOR x;
        VECTOR x_prev; */
    const int npoints;
    const int ntrials;
    const double freq;
    const double N;
    const bool discrete;

    VECTOR t;
    VECTOR_OF(MATRIX) x;
    const double dt;

    int timeIndex, tTimeIndex, pN, trial;
    double tempM, xEst;

    TimeSeries(BaseMethod& sm_, int np_, int nt_,
                double freq_, double N_=1.0, bool discrete_=true):
        sm(sm_), complete(false), npoints(np_), ntrials(nt_),
        freq(freq_), N(N_), discrete(discrete_),
        t(np_), x(nt_), dt(1.0/freq_)
    {
        trial = 0;
        trace("TimeSeries(METHOD:%s) executed.\n", sm.name);
    }
    void new_trial() {
        timeIndex = 0;
        t[timeIndex] = sm.time;
        x[trial].resize(npoints, sm.x.dim());
        for (int pN = 0; pN < sm.x.dim(); ++pN) {
            x[trial](timeIndex, pN) = sm.x[pN]/N;
        }
        ++timeIndex;
        trace("TimeSeries.new_trial() executed.\n");
    }
    bool process_info() {
        while (timeIndex < npoints && t[timeIndex-1] + dt <= sm.time) {
            t[timeIndex] = t[timeIndex-1]+dt;
            for (int pN = 0; pN < sm.x.dim(); ++pN) {
                tempM = (sm.x[pN] - sm.x_prev[pN])/sm.time_step;
                if (!discrete) {
                    xEst = tempM*(t[timeIndex] - sm.time)+sm.x[pN];
                } else if (tempM > 0) {
                    xEst = floor(tempM*(t[timeIndex] - sm.time)+sm.x[pN]);
                } else {
                    xEst = ceil(tempM*(t[timeIndex] - sm.time)+sm.x[pN]);
                }
                // (t[timeIndex], xEst) is ready.
                // This is a point in the simulation. Store it.
                x[trial](timeIndex, pN) = xEst/N;
            }
            ++timeIndex;
        }
        if (timeIndex >= npoints) {
            trace("TimeSeries.processInfo()is done.\n");
            complete = true;
            return true;
        }
        trace("TimeSeries.process_info() executed.\n");
        return false;
    }
    void end_trial() {
        while (timeIndex < npoints) {
            t[timeIndex] = t[timeIndex-1]+dt;
            for (int pN = 0; pN < sm.x.dim(); ++pN) {
                x[trial](timeIndex, pN) = sm.x[pN]/N;
            }
            ++timeIndex;
        }
        trial++;
        complete = false;
        trace("TimeSeries.end_trial() executed.\n");
    }
    void end_sim() {
        trace("TimeSeries.end_sim() executed.\n");
    }
    bool is_complete() const {
        trace("TimeSeries.complete() executed: %s\n", 
              (complete ? "true": "false"));
        return complete;
    }
};

#endif
