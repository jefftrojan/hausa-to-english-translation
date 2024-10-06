### **Hausa-to-English translator using RNN**

---

This project uses data that has been webscraped from twitter and preprocessed to have parallel data which is then used for translation operations.

#### **1. Data Preparation**

I started by preparing a parallel dataset that contained Hausa-to-English translations of tweets. The dataset included four key columns: `CleanedMainT` (the main tweets), `CleanedReplyT` (replies to tweets), and their corresponding English translations (`Hausa2EngMainT` and `Hausa2EngReplyT`).

Before diving into the model training process, I spent time cleaning and preprocessing the text data:

- **Text Cleaning**: I applied a custom text preprocessing function to remove unwanted characters such as punctuation, URLs, and extra spaces from both `CleanedMainT` and `CleanedReplyT`.
- **Handling Missing Data**: To avoid issues during training, I used `fillna('')` to replace missing values and ensured that all entries were converted to strings. This prevented any non-string data from breaking the model later on.

---

#### **2. Model Design**

For this task, I decided to use a Recurrent Neural Network (RNN) based **Encoder-Decoder model with Attention** for translating Hausa to English. The choice of model stemmed from its effectiveness in handling sequence-to-sequence problems like translation.

- **Encoder**: I used a series of RNN layers to process the input sequence (Hausa tweets) and convert them into fixed-size context vectors.
- **Attention Mechanism**: To improve translation accuracy, I incorporated an attention mechanism, which allows the model to focus on relevant parts of the input sequence when generating each word in the output sequence.
- **Decoder**: The decoder consists of RNN layers as well, taking the context vectors from the encoder along with the attention output and generating the translated English sentences.

---

#### **3. Training Procedure**

To train the model, I used the following steps:

- **Data Splitting**: The dataset was split into training, validation, and test sets. The training data was used to fit the model, and the validation data helped monitor performance during training to avoid overfitting.
- **Tokenization**: I tokenized both Hausa and English texts into word indices using Keras' `Tokenizer`. This tokenization step was essential for feeding sequences into the RNN layers.
- **Loss Function**: I used categorical cross-entropy as the loss function, as this is commonly used in sequence-to-sequence models for translation tasks.
- **Optimizer**: I chose Adam optimizer, which is widely used in NLP models for its ability to adapt learning rates dynamically.
- **Batch Size and Epochs**: I trained the model for several epochs with an appropriate batch size to strike a balance between performance and computation time.

---

#### **4. Evaluation Metrics**

To assess the model's performance, I used the following metrics:

- **BLEU Score**: The Bilingual Evaluation Understudy (BLEU) score was used to evaluate the quality of the translation by comparing the generated translation with reference translations.
- **Accuracy**: I also tracked word-level accuracy to see how often the model was predicting the correct words in the sequence.
- **Loss**: The training and validation loss were monitored throughout the training process.

---

#### **5. Visualizations**

As part of my analysis, I generated visualizations to explore common terms in both the original Hausa tweets and their English translations:

- **Word Cloud Visualization**: I created word clouds to represent the most frequent terms in both the main tweets and the replies. This gave insights into the key terms in the dataset, such as `bindiga` (gunmen) and `za` (will), which appeared frequently.

---

#### **6. Conclusion**

In this project, I built an RNN-based translation model using the Encoder-Decoder architecture with Attention. The model was trained on a cleaned dataset of Hausa-to-English tweets, and its performance was evaluated using BLEU scores, accuracy, and loss metrics. Additionally, visualizations helped in understanding the linguistic patterns present in the dataset.

This process allowed me to deepen my understanding of NLP tasks, sequence modeling, and how attention mechanisms can enhance translation tasks.

---


#### **7. References**
1. Isa Inuwa-Dutse, (2021). The first large scale collection of diverse Hausa language datasets. Retrieved from https://www.semanticscholar.org/reader/6995aff0c181ef6c8236b7e9cc27af8ddcf935a1
2. Bahdanau, D., Cho, K., & Bengio, Y. (2015). Neural Machine Translation by Jointly Learning to Align and Translate. *arXiv preprint arXiv:1409.0473*. Retrieved from https://arxiv.org/abs/1409.0473
3. Keras Documentation: RNN Layers. Available at: https://keras.io/api/layers/recurrent_layers/
4. TensorFlow Documentation: Neural Machine Translation with Attention. Available at: https://www.tensorflow.org/tutorials/text/nmt_with_attention
5. Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global Vectors for Word Representation. *EMNLP 2014*. Retrieved from https://nlp.stanford.edu/pubs/glove.pdf


