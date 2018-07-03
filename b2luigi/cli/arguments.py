import argparse


def get_cli_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("--show-output",
                        help="Instead of running the tasks, show which output files will/are created.",
                        action="store_true")
    parser.add_argument("--test",
                        help="Run the task list in test mode by printing the log directly to the screen instead"
                             "of storing it in a file.",
                        action="store_true")
    parser.add_argument("--batch",
                        help="Instead of running locally, try to submit the tasks to the batch system.",
                        action="store_true")
    parser.add_argument("--batch-runner",
                        help="Expert option to mark this worker as a batch runner.",
                        action="store_true")
    parser.add_argument("--scheduler-host",
                        help="If given, use this host as a central scheduler instead of a local one.", default="")
    parser.add_argument("--scheduler-port",
                        help="If given, use the port on this host as a central scheduler instead of a local one.",
                        type=int,
                        default=0)

    args = parser.parse_args()

    if args.test and (args.scheduler_host or args.scheduler_port):
        raise AttributeError("Can not test while using a central scheduler!")
    if args.batch and (not args.scheduler_host and not args.scheduler_port):
        raise AttributeError("If you want to use the batch submission, you have to start a central scheduler first.")
    if args.batch_runner and (not args.scheduler_host or not args.scheduler_port):
        raise AttributeError("A batch runner should always have a fully qualified port and "
                             "host name for the central scheduler.")
    if args.show_output and (args.scheduler_host or args.scheduler_port or args.batch or args.test):
        print("Ignoring all other parameters, as you have given the --show-output parameter.")

    return args
