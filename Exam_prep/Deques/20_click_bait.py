from collections import deque

final_feed_collection = []
suggested_links = deque(map(int, input().split()))
featured_articles = list(map(int, input().split()))
engagement_value = int(input())

while suggested_links and featured_articles:
    current_suggested_links = suggested_links.popleft()
    current_featured_articles = featured_articles.pop()

    if current_suggested_links > current_featured_articles:
        remainder = current_suggested_links % current_featured_articles
        final_feed_collection.append(-remainder)

        if remainder != 0:
            suggested_links.append(remainder * 2)

    elif current_suggested_links == current_featured_articles:
        final_feed_collection.append(0)

    else:  # current_suggested_links < current_featured_articles
        remainder = current_featured_articles % current_suggested_links
        final_feed_collection.append(remainder)

        if remainder != 0:
            featured_articles.append(remainder * 2)

total_value = sum(final_feed_collection)

print(f'Final Feed: ', end='')
final_feed_collection = list(map(str, final_feed_collection))
f = ', '.join(final_feed_collection)
print(f, end='')
print()

if total_value >= engagement_value:
    print(f'Goal achieved! Engagement Value: {total_value}')
else:
    print(f'Goal not achieved! Short by: {engagement_value - total_value}')


