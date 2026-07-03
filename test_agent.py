from groq_agent import generate_curriculum

data, usage = generate_curriculum("Social Media Marketing", "Beginner", 3, "Fast Draft (8B)")
print(data)
print(usage)