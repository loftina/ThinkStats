import Cdf
import relay
import myplot as mplt

def main():

    #Exercise 3.5
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    speedsCdf = Cdf.MakeCdfFromList(speeds, "race speeds")
    mplt.Cdf(speedsCdf)
    mplt.show(title="Race Speed CDF", xlabel="speed in mph", ylabel="probability")

if __name__ == "__main__":
    main()