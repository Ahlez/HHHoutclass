import streamlit as st
import pandas as pd
import pickle
import sklearn
from sklearn import prepocessing

loaded_model = pickle.load(open("sales-advertising-model.h5","rb")
