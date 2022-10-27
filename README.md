# Exogenous saving economy model simulation

In this program we construct and perform a simple simulation of an Exogenous productivity shock to an economy with Exogenous savings. We suppose that the productivity follows a AR1 process

We have the following equations that define our model:

1. Production function:

$$y_t=a_tk_t^{\phi} $$

2. Capital Movement:

$$k_{t+1}=k_t^{1-\delta}{inv_t}^{\delta}$$

3. Economy Demand:

$${inv_t}=y_t^{\gamma}$$

4. Productivity process AR1:

$$ln(a_{t+1})= \rho_aln(a_t)+\sigma_a\epsilon_{a,t+1}$$

The VAR for this model can be describe like:

$$x_{t+1}=A_0x_t+C\epsilon_{a,t+1}$$

Where:

$$x_t=\begin{bmatrix}
ln(y_{t-1}) \\
ln(k_t) \\
ln(a_t)
\end{bmatrix}$$

$$ A_0=\begin{bmatrix}
0 & \phi & 1 \\
0 & 1-\delta+\gamma\delta\phi & \gamma\delta \\
0 & 0 & \rho_a
\end{bmatrix}  $$

$$C=\begin{bmatrix}
0 \\
0 \\
\sigma_a
\end{bmatrix}$$

We assume the following calibration:

$$\phi=0.5;
\rho_a=0.9;
\delta=0.02;
\sigma_a=0.02;
\gamma=0.5$$

In the first part of the code we set a $k_1=0.3$

With this initial value we simulate the model to see it converge.

In the second part of the code we start in the stationary level and perform a shock of 1 standard deviation in the productivity.
