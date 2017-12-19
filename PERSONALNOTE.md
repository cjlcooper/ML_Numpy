# Machine Learning With Numpy

#### Ndarray对象
1.NumPy中定义的最重要的对象是称为ndarray的N维数组类型;</br>
2.ndimin 指定返回数组的最小维数;</br>
3.ndarray 对象由计算机内存中的一维连续区域组成;</br>

#### Ndarray属性
1.shape:获取矩阵的行数和列数->(行数， 列数),shape也可以调整矩阵的行数和列数;</br>
2.ndim:返回数组的维数;<br/>
3.itemsize:返回数组中每个元素的字节单位长度;<br/>
4.flags:返回了数组的属性值;<br/>
5.empty和dtype:产生一个指定行列数的随机矩阵，dtype指定元素类型;<br/>
6.zeros:返回特定大小，以 0 填充的新数组,zeros((5,6));<br/>
7.ones:返回特定大小，以 1 填充的新数组,ones((2,3));<br/>

#### 来自现有数据的数组
1.asarray:将Python序列转换为ndarray,例如:asarray(序列);<br/>
2.frombuffer:将缓冲区解释为一维数组,例如:frombuffer(字符串, dtype = 'S1');<br/>
3.