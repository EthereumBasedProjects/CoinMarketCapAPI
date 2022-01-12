import sys
import coinMarketCap.connect
import slackConnect.connect

btcDominance = coinMarketCap.connect.getBTCDominance()
message = ":btc: *Bitcoin Dominance:* " + str(btcDominance) + "\n"

if (btcDominance <= 38):
    message += ":alert: :alert: :alert: *PANIC!!!!! OH SHIT!!!! Bitcoin Dominance is less than 38%!*"
elif (btcDominance <= 39):
    message += ":alert: :alert: *PANIC????? OH SHIT!!!! Bitcoin Dominance is less than 39%!*"
elif (btcDominance <= 40):
    message += ":alert: *WATCH!!!!! Bitcoin Dominance is less than 40%!*"

#if (btcDominance <= 40):
slackConnect.connect.post_message_to_slack(message)
