#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - zombies
 *
 * Description: make five zombies
 * Return: 0 for success
 */
int main(void)
{
	int i;
	pid_t zombie_pid;

	i = 0;
	while (i < 5)
	{
		zombie_pid = fork();
		if (zombie_pid)
			printf("Zombie process created, PID: %i\n", zombie_pid);
		else
			exit(0);
		i++;
	}
	sleep(100);
	return (0);
}
