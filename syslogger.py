# coding=utf-8
import sys


class SysLogger:
    progress = ''

    def write_iteration_name(self, iteration_name):
        """Writes iteration name (printed out before the progress).
        :param string iteration_name: Iteration name
        """
        self.progress = ''
        sys.stdout.write("\n%s: " % iteration_name)

    def write_progress(self, current_step, total_steps):
        """Writes current progress
        :param int current_step: Current step
        :param int total_steps: Total steps count
        """
        if self.progress != '':
            sys.stdout.write("\b" * len(self.progress))

        self.progress = "%s / %s" % (current_step, total_steps)
        sys.stdout.write(self.progress)
        sys.stdout.flush()
