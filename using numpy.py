import numpy as np
np1=np.array([1,2,3,4])
np2=np.array([1,2,3,4])
np3=np1*np2
type(np1) 

#find minimum,maximum,square root
import numpy as np
b=np.array([10,20,30,40])
print(np.max(b))
print(np.min(b))
print(np.sqrt(b))

#to find shape,dimension
import numpy as np
ab=np.array([[[11,22,33,44],[55,66,77,88],[111,222,333,444]]])
print(np.ndim(ab))

a=np.array([[1,2,7,3,2,7,9],[2,3,4,5,6,1,2]])
print(np.ndim(a))
print(a.shape)
print(a.reshape(7,2))
