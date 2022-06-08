import main
import test_engine

a = main.np.array([1.,1.,2.,])

test_engine.test(main.T(0.,a),2.)
test_engine.test(main.T(1,a),4.)
test_engine.test(main.T(-2,a),4.)