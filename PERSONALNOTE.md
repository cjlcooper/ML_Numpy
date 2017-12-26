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
3.fromiter:从任何可迭代对象构建一个ndarray对象，返回一个新的一维数组;<br/>
4.arange:创建一个序列0到n的一维矩阵,例如:arange(n);<br/>
5.linspace:<br/>
6.logspace:<br/>

# Matplotlib Note
1.Matplotlib 是 Python 的绘图库;<br/>
2.pyplot()是 matplotlib 库中最重要的函数，用于绘制 2D 数据;<br/>

# About Python

1.类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self:<br/>
<<<<<<< HEAD
例如：
def function1(self):
2.sigmoid函数：既S型的函数,例如对数函数
3.shape[0]:获取第一维的长度,以此类推到n维长度;
=======
例如：<br/>
def function1(self):<br/>
2.sigmoid函数：既S型的函数,例如对数函数;<br/>

# About Matrix
#### 矩阵的逆（逆矩阵）
设A是数域上的一个n阶方阵，若在相同数域上存在另一个n阶矩阵B，使得： AB=BA=E。 则我们称B是A的逆矩阵，而A则被称为可逆矩阵。
E为单位矩阵。<br/>
#### 单位矩阵
从左上到右下的对角线全部为1的矩阵。<br>
>>>>>>> 2ff1185d0064c2f1d362806974e4e0c4908ea67f
