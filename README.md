# Text-Network Analysis

Automatic pipeline for creating and visualizing text networks. It helps filter and group the most important words in the corpus by the means of centrality and community graph measures. It's and end-to-end solution that takes a text corpus as an input, and gives a visualized filtered graph with the most important words for interpretation, without the need of using any external software.

The tool is based on the work described in [1](http://www.ijssh.org/papers/459-CH357.pdf). Please cite this paper if you found this code useful.

## Dependencies

The code is written in python. The dependencies are:
* Python 3.6
* Networkx
* Matplotlib

## Example usage

An example corpus of 1.2 million tokens from PubMed open abstracts on cancer is included. To create and visualize a graph based on this corpus, simply run:

```python
python tna.py
```

It takes around 15 minutes to process the corpus on a desktop computer (2.2Ghz, 16gb of RAM). After the calculations are done, you should get a visualization presented below:

![graph.png](https://github.com/michal-pikusa/text-network-analysis/graph.png)

## TODO

It is not a final version, as it does not modify the colors and size of the nodes. These features will be added to reflect the work presented in the aforementioned paper.

## Reference

[1] M. Gruszecka & M. Pikusa. 2015. "Using Text Network Analysis in Corpus Studies--A Comparative Study on the 2010 TU-154 Polish Air Force Presidential Plane Crash Newspaper Coverage". International Journal of Social Science and Humanity.
