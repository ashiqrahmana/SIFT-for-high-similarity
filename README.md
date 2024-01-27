# Skiptrace - Identifying Associates for Professor Moriarty's Defeat

## Task Description
Sherlock Holmes, in his pursuit to defeat Professor Moriarty, has been recommended three associates by Irene Adler. Irene provided pictures of their last known whereabouts. Your task is to identify these associates by matching the provided query pictures with a database of surveillance photos around NYC. Each associate is known to appear at least once in the surveillance photos.

## Requirements and Tips
1. **Time and Memory Consideration:**
   - This task can be time-consuming and memory-intensive.
   - The provided script was tested on a laptop with 16GB of RAM and a Ryzen 9 5900HS CPU, taking approximately 50 minutes to complete.
   - Consider starting the task early.

2. **Concatenation Consideration:**
   - Avoid frequent use of `np.vstack()`, `np.hstack()`, or `np.concatenate()` as resizing numpy arrays can be time and memory-consuming.
   - Explore alternative options in Python for array concatenation.

## Functions and Directory Paths
### Functions:
1. **extract_sift_features:**
   - Takes an image path as input, reads the image in grayscale, and extracts SIFT features (keypoints and descriptors).
   
2. **match_features:**
   - Takes query descriptors and database descriptors, matches them using the Brute-Force matcher, and applies a ratio test to filter good matches.

### Directory Paths:
- **query_dir:**
   - Directory path containing the query images (pictures of associates provided by Irene Adler).
   
- **database_dir:**
   - Directory path containing the NYC surveillance photos.

### Image File Listing:
- Lists files in the query and database directories, considering only those with file extensions '.jpg' or '.png'.

## Matching Process
1. Iterates through each query image and each database image.
2. Extracts SIFT features for both the query and database images.
3. Matches the features using the `match_features` function and calculates a similarity score.

## Results
- The results are stored in a list called `results`, containing dictionaries with information about the query image, database image, and the similarity score.

## Display of Top Results
- The script displays the top 5 matching results for each query image.

## Code Results
- Top 5 Results for each query image are presented, showing the corresponding database image and similarity score.

## Code Implementation
```python
# Place the provided code here
```

## Conclusion
The script provides insights into the potential associates recommended by Irene Adler based on the surveillance photos. The top-corresponding images for each query are displayed, allowing further investigation into the identities of these associates. The success of Sherlock Holmes in defeating Professor Moriarty may depend on the accuracy of these identifications.

**Author:** Ashiq Rahman Anwar Batcha, NetID: aa10277
