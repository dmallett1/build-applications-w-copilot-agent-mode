import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://friendly-xylophone-x54vg49qwgx3p4xg-8000.app.github.dev/api-root/activity/')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div>
      <h1>Activities</h1>
      <ul>
        {activities.map(activity => (
          <li key={activity.id}>{activity.type} - {activity.duration} minutes</li>
        ))}
      </ul>
    </div>
  );
}

export default Activities;