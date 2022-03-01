
"""Help module of command line"""

def help_func():
    """help options"""
    print("\n Usage: \n")
    print("\t python website_stats.py [command] [Argument] \n ")
    print("Available Commands: \n")
    print(
        "\t crawl [urlname] [...] \n"
        "\t \t -> This command collects all the statistics of a website passed as argument."
    )
    print("\t \t -> It takes a valid website URL as argument. \n")
    print(
        "\t list-reports \n \t \t -> This command lists the report snapshot of each crawled website."
    )
    print(
        "\t \t -> It does not take any argument, just lists all the crawled websites \n"
    )
    print(
        """\t links-report [reportid] [data format]\n
        \t links-report [reportid]      - generates yaml report (default) 
        \t links-report [reportid] html - generates html report 
        \t links-report [reportid] json - generates json report 
        \t links-report [reportid] csv  - generates csv report \n 
        \t -> This command lists all the links report of a specific website crawl operation."""
    )
    print("\t \t -> This command takes the report id as the argument. \n"
    )
