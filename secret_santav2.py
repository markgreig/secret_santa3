#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import random

def secret_santa_pairing(members):
    shuffled_members = members.copy()
    random.shuffle(shuffled_members)
    pairs = []
    for i in range(len(members)):
        if members[i] == shuffled_members[i]:
            return secret_santa_pairing(members)  # Retry if someone is paired with themselves
        pairs.append((members[i], shuffled_members[i]))
    return pairs

st.title('Secret Santa Pairing Generator')

if 'pairs' not in st.session_state:
    st.session_state['pairs'] = []

members = ['Duncan', 'Chris', 'Lucy', 'Patrick', 'Mohammed']

if st.button('Generate Secret Santa Pairs'):
    st.session_state['pairs'] = secret_santa_pairing(members)

if st.session_state['pairs']:
    st.write('Here are the Secret Santa pairs:')
    for pair in st.session_state['pairs']:
        st.write(f'{pair[0]} -> {pair[1]}')

