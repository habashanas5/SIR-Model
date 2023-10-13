import matplotlib.pyplot as plt

# Initial conditions and constants
susceptibles = 762
transmission_constant = 0.00218
infecteds = 1
recovery_rate = 0.5
recovereds = 0

dt = 0.01
duration = 20
iteration = int(duration/dt)

S = []
I = []
R = []
t = 0

for i in range(iteration):
    get_sick = transmission_constant * susceptibles * infecteds
    recover = recovery_rate * infecteds
    susceptibles -= get_sick * dt
    infecteds += (get_sick - recover) * dt
    recovereds += recover * dt
    t = i * dt
    S.append(susceptibles)
    I.append(infecteds)
    R.append(recovereds)


plt.figure(figsize=(10,8))
plt.plot(S, label='Susceptibles', color = "red")
plt.plot(I, label='Infecteds', color = "blue")
plt.plot(R, label='Recovereds', color = "black")
plt.xlabel('time')
plt.ylabel('Population')
plt.title('SIR Model Simulation')
plt.legend()
plt.grid(True)
plt.show()
