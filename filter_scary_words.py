import re

"""
This regular expression will match any word that contains one of the words on the scary_words_list variable.
The sub() function will then replace all the matches with an empty string, which will effectively remove the scary words from the text.
"""
def filter_scary_words(text):
  """Returns a copy of the text with all the scary words removed."""
  scary_words_regex = re.compile(r"\b" + "|".join(scary_words_list) + r"\b")
  filtered_text = scary_words_regex.sub("", text)
  return filtered_text
