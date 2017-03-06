(ns wordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetcount [options]
   [
    ;; spout configuration
    {"sentence-spout" (python-spout-spec
          options
          "spouts.sentences.Sentences"
          ["sentence"]
          )
    }
    ;; bolt configuration
    {
     ;; parse-bolt
     "parse-bolt" (python-bolt-spec
          options
          {"sentence-spout" :shuffle}
          "bolts.parse.ParseTweet"
          ["words"]
          :p 2
          )
     ;; count-bolt
     "count-bolt" (python-bolt-spec
         options
         {"parse-bolt" ["words"]}
         "bolts.tweetcounter.TweetCounter"
         ["word" "count"]
         :p 1
         )
    }
  ]
)
