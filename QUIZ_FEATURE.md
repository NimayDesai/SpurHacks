# Quiz Feature Documentation

## Overview

The quiz feature generates multiple choice questions based on educational scripts created by the AI presentation system. This allows users to test their understanding of the material after watching presentations.

## Architecture

### Backend Implementation

#### New Endpoint: `/api/gemini/generate-quiz`

**Location:** `SpurHacks/backend/routes/gemini.py`

**Method:** POST

**Request Body:**
```json
{
    "script": "Educational script content here...",
    "num_questions": 5
}
```

**Response:**
```json
{
    "success": true,
    "quiz": {
        "questions": [
            {
                "id": 1,
                "question": "What is the main process by which plants convert light energy?",
                "options": {
                    "A": "Respiration",
                    "B": "Photosynthesis",
                    "C": "Transpiration",
                    "D": "Germination"
                },
                "correct_answer": "B",
                "explanation": "Photosynthesis is the process by which plants convert light energy into chemical energy using chlorophyll."
            }
        ]
    }
}
```

#### Implementation Details

1. **AI Generation:** Uses Google Gemini API to analyze the educational script and generate relevant questions
2. **Question Format:** Multiple choice with 4 options (A, B, C, D)
3. **Validation:** Server validates question structure and ensures all required fields are present
4. **Error Handling:** Comprehensive error handling for API failures, invalid JSON, and missing data

### Frontend Implementation

#### Components

1. **QuizDisplay Component** (`SpurHacks/frontend/src/components/quiz-display.tsx`)
   - Displays individual questions with multiple choice options
   - Provides immediate feedback on answers
   - Shows progress through the quiz
   - Displays final score and review of incorrect answers
   - Supports retaking the quiz

2. **PresentationDisplay Integration** (`SpurHacks/frontend/src/components/chat-interface.tsx`)
   - Adds quiz section to existing presentations
   - "Generate Quiz" button to create questions from the script
   - Seamless integration with AI tutor and video content

#### Features

- **Interactive Questions:** Click to select answers with visual feedback
- **Immediate Feedback:** Shows correct/incorrect status with explanations
- **Progress Tracking:** Visual progress bar and question counter
- **Score Display:** Shows running score and final percentage
- **Review Mode:** After completion, shows all incorrect answers with explanations
- **Retake Options:** Users can retake the same quiz or generate a new one

## User Flow

1. **Presentation Generation:** User requests an educational presentation on any topic
2. **Content Display:** System shows script, AI tutor, and video animation
3. **Quiz Generation:** User clicks "Generate Quiz" button
4. **Question Display:** Quiz shows one question at a time with 4 options
5. **Answer Selection:** User selects an answer and receives immediate feedback
6. **Progress:** User moves through all questions at their own pace
7. **Results:** Final score is displayed with review of incorrect answers
8. **Retake:** User can retake the quiz or generate new questions

## Technical Features

### Backend Features

- **Flexible Question Count:** Configurable number of questions (default: 5)
- **Content Analysis:** AI analyzes script to identify key concepts
- **Quality Assurance:** Validates question structure and answer options
- **Error Recovery:** Handles API failures gracefully
- **Performance:** Efficient question generation with reasonable timeouts

### Frontend Features

- **Responsive Design:** Works on desktop and mobile devices
- **Accessibility:** Keyboard navigation and screen reader support
- **Visual Feedback:** Color-coded answers (green for correct, red for incorrect)
- **State Management:** Tracks user progress and answers
- **Smooth Transitions:** Animated feedback and progress updates

## Testing

### Test Script

Location: `SpurHacks/backend/test_quiz_generation.py`

Run with:
```bash
cd SpurHacks/backend
python test_quiz_generation.py
```

### Test Cases

1. **Valid Script:** Tests successful quiz generation with sample content
2. **Empty Script:** Validates error handling for empty input
3. **Missing Script:** Tests API response for missing required fields
4. **Large Content:** Tests with longer educational scripts

## Integration Points

### Existing Systems

- **Gemini API:** Uses same configuration as presentation generation
- **Chat Interface:** Integrated as additional card in presentation display
- **UI Components:** Reuses existing Button, Card, and other UI elements
- **State Management:** Follows same patterns as other React components

### Dependencies

#### Backend
- `google.generativeai` - For AI question generation
- `flask` - Web framework
- `json` - Response parsing and validation

#### Frontend
- `react` - Component framework
- `next.js` - Application framework
- UI components from `@/components/ui/`
- Icons from `lucide-react`

## Configuration

### Environment Variables

No additional environment variables required - uses existing Gemini API configuration.

### Default Settings

- **Default Questions:** 5 per quiz
- **Question Format:** Multiple choice (A, B, C, D)
- **Timeout:** 30 seconds for API requests
- **Passing Score:** 70% (visual indicator only)

## Future Enhancements

1. **Question Types:** Support for true/false, fill-in-the-blank
2. **Difficulty Levels:** Easy, medium, hard question generation
3. **Analytics:** Track user performance over time
4. **Adaptive Testing:** Adjust difficulty based on user performance
5. **Export Options:** Download quiz results or questions
6. **Collaborative Features:** Share quizzes with other users
7. **Time Limits:** Optional time constraints for questions
8. **Categories:** Tag questions by topic or subject area

## Error Handling

### Common Errors

1. **API Timeout:** Quiz generation takes too long
2. **Invalid JSON:** Malformed response from AI
3. **Missing Fields:** Incomplete question structure
4. **Network Issues:** Connection problems with backend

### User Messages

- Clear error messages for all failure scenarios
- Retry options for temporary failures
- Graceful degradation when features unavailable

## Performance Considerations

- **Caching:** Consider caching generated quizzes for repeated requests
- **Lazy Loading:** Quiz component loads only when needed
- **Debouncing:** Prevent multiple simultaneous quiz generation requests
- **Memory Management:** Clean up quiz state when component unmounts

## Security

- **Input Validation:** Server validates all input parameters
- **Rate Limiting:** Prevents abuse of quiz generation endpoint
- **Content Filtering:** AI naturally filters inappropriate content
- **No Authentication Required:** Public educational feature

## Accessibility

- **Keyboard Navigation:** Full keyboard support for all interactions
- **Screen Readers:** Proper ARIA labels and semantic HTML
- **Color Contrast:** High contrast for answer feedback
- **Focus Management:** Clear focus indicators throughout quiz

This quiz feature enhances the educational value of the AI presentation system by providing interactive assessment capabilities that help reinforce learning and measure comprehension.