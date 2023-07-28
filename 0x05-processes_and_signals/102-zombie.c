#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>

int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

int main(void)
{
	pid_t pid, child_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
	pid = fork();
	if (pid == -1)
	{
	printf("Could not fork a child process\n");
	exit (0);
	}
	if (pid == 0)
	{
	child_pid = getpid();
	printf("Zombie process created, PID: %i\n", child_pid);
	infinite_while();
	exit (0);
	}
	}
	sleep(2);
	return (0);
}
