#plot(path_planning$D_distance, type="o", col="blue", xlab = "Map Number", ylab = "Path Distance (m)", ylim = c(20, 35), main = "Distance of Paths planned by Dijkstra and A*")
#lines(path_planning$`A*_distance`, type="o", pch=22, lty=2, col="red")
#legend(1, 32, legend=c("A*", "Dijkstra"), col=c("red", "blue"), lty=2:1, cex=0.8)

plot(path_planning$D_time, type="o", col="blue", xlab = "Map Number", ylab = "Consumed Time (sec)", main = "Time consumption of Path-planning by Dijkstra and A*", ylim = c(0, 30))
lines(path_planning$`A*_time`, type="o", pch=22, lty=2, col="red")
legend(1, 28, legend=c("A*", "Dijkstra"), col=c("red", "blue"), lty=2:1, cex=0.8)

