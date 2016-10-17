(ns specialrel.core)

(def c 299792458) ;; Speed of light constant

(defn ctometer [x] ;; converts to meters per second
  (* x c))

(defn metertoc [x] ;; converts meters per second to terms of c
  (float (/ x c)))

(defn gamma [v]   ;; calculates the gamma factor depending on the velocity in terms of c
  (/ 1 (float (Math/sqrt (- 1 (* v v))))))

(defn ctogamma [v]  ;; converts to gamma depending on the velocity in terms of meters per second
  (gamma (float (metertoc v))))

(defn xlorentz [speed x t]  ;; Does a lorentz transformation for space
  (* (gamma speed) (- x (* speed t))))

(defn tlorentz [speed x t]  ;; Does a lorentz transformation for time
  (* (gamma speed) (- t (* speed x))))

(defn vlorentz [v w]  ;; Lorentz transformation for velocity
  (/ (- v w) (- 1 (* v w))))

(defn lorentz [speed x t]  ;; Lorentz transformation for both space and time
  (let [x (xlorentz speed x t)
        t (tlorentz speed x t)]
    (println "x'=" x "  t'=" t)
    [x, t]))

(defn timedialation [v t]  ;; Calculates the time dialation given the velocity and time
  (* t (gamma v)))

(defn lengthcontraction [v h] ;; Calculates the length contraction based on velocity and length
  (/ h (gamma v)))

(defn spacetimeinterval [x t] ;; calculates the spacetime interval given the space and time in meters.
  (Math/sqrt (- (* t t) (* x x))))

(defn spaceinterval [x1 x2]
  (- x2 x1))

(defn timeinterval [t1 t2]
  (t2 - t1))

(defn spacetimeinterval2 [t1 t2 x1 x2]
  (Math/sqrt (- (Math/pow (- t2 t1) 2) (Math/pow (- x2 x1) 2))))
