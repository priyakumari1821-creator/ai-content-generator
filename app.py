# AI Content Generator using Claude (Demo Project)

def generate_linkedin_post(topic):
    return f"""
🔥 Here's something powerful about {topic}:

Most people ignore this, but {topic} is changing the way we work and think.

💡 Key insight:
Consistency + smart tools = real growth

Start using AI to improve your daily workflow and productivity.

#AI #Productivity #LinkedInGrowth
"""

def generate_instagram_caption(topic):
    return f"""
✨ {topic} vibes ✨

Level up your content using AI tools like Claude 🚀

#contentcreation #AItools #growth
"""

# Demo usage
if __name__ == "__main__":
    topic = "AI Tools"
    print("LinkedIn Post:")
    print(generate_linkedin_post(topic))

    print("\nInstagram Caption:")
    print(generate_instagram_caption(topic))
