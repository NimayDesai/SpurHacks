# Numina – Your Last-Minute Study Superpower

## Inspiration  
We're a bunch of high school students who always end up cramming the night before a big exam. We wanted a faster, smarter way to actually *understand* concepts instead of just searching random videos or reading long PDFs. That’s why we created **Numina**—an AI-powered tutor that explains anything through animated videos and lets you test your understanding instantly.

## What it does  
Numina is a full-stack learning platform that turns any confusing topic into:  
1. A narrated 3Blue1Brown-style animation  
2. A live AI tutor who can talk with you via **voice-to-voice conversation**  
3. A custom quiz and flashcard set to help you retain what you learned  

It’s like having your own personal tutor, animator, and exam coach—all in one app.

## How we built it  

### Backend  
- **Flask + SocketIO** for the real-time engine  
- **Gemini + Claude AI** for generating educational scripts and Manim code  
- **Manim + FFmpeg** to render animated videos on the fly  
- **Tavus API** to generate personalized, talking AI tutors  
- **JWT Authentication** for secure user login  
- Quiz/flashcard generation using LLM-based evaluation

### Frontend  
- Built with **Next.js + React + Tailwind CSS**  
- Integrated **video playback**, **live chat**, **AI voice tutor**, and **interactive quizzes**  
- **WebRTC** used to support seamless real-time interaction  
- Smooth UI/UX designed for last-minute study sessions

## Challenges we ran into  
- Making AI-generated scripts sync perfectly with Manim visuals  
- Supporting real-time video rendering without crashing the server  
- Building natural voice-to-voice AI conversations  
- Creating accurate auto-generated quizzes based on unique scripts

## Accomplishments that we're proud of  
- Fully automated learning pipeline from “topic” to **video + live AI tutor + quiz**  
- Voice conversations that feel human and informative  
- Flashcards and quizzes that reinforce retention—no extra work for users  
- Actually useful for us during real exam prep!

## What we learned  
- How to combine multiple AI services into a smooth educational experience  
- The power of real-time rendering and natural voice interaction  
- Making education tools fun and efficient at the same time  
- How to design a learning flow that works even when you’re cramming

## What's next for Numina  
- Let users upload class notes and convert them to videos/quizzes automatically  
- Launch a mobile app for portable cramming  
- Improve voice interaction to include real-time emotion/context detection  
- Add collaborative study rooms with shared AI tutors
