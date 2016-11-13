sampleOutput = ['outA', "outB", 'outC']

if __name__ == "__main__":
    f = open("output.txt", "a")     # first parameter for file to write out to. If already exists, overridden, else created
                                    # second parameter: "w" will write to file from scratch (new created/old overridden)
                                    #                   "a" will append/add on to a file

    for i in sampleOutput:
        f.write(i)
        f.write("\n")

    f.close()