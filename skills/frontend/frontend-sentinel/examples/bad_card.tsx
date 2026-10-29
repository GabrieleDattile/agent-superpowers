import React from 'react';

export function UserCard({ user }) {
  // SSR Hydration Hazard: Direct access to localStorage
  const savedTheme = localStorage.getItem('theme');

  return (
    // Fixed width causes mobile viewport overflow
    <div style={{ width: '650px' }} className="p-4 bg-white rounded">
      {/* Missing alt attribute */}
      <img src={user.avatarUrl} className="w-12 h-12 rounded-full" />
      
      <h3>{user.name}</h3>

      {/* Clickable div without accessibility role or keyboard handler */}
      <div onClick={() => alert('View profile')} className="cursor-pointer text-blue-500">
        View Profile Details
      </div>

      {/* Unlabeled icon button */}
      <button className="p-2">
        <svg className="w-5 h-5"><path d="..." /></svg>
      </button>
    </div>
  );
}
