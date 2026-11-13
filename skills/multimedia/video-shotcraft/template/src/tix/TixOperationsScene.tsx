import React from 'react';
import { AbsoluteFill, Img, interpolate, staticFile, useCurrentFrame, Easing } from 'remotion';

export const TixOperationsScene: React.FC<{ duration: number }> = ({ duration }) => {
  const frame = useCurrentFrame();

  const fadeIn = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const fadeOut = interpolate(frame, [duration - 10, duration], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const manifestX = interpolate(frame, [0, 22], [80, 0], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const scannerScale = interpolate(frame, [8, 26], [0.88, 1], {
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  const scannerT = interpolate(frame, [8, 26], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  const badge1T = interpolate(frame, [22, 38], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: '#070b14',
        overflow: 'hidden',
        opacity: fadeIn * fadeOut,
      }}
    >
      {/* Background ambient lighting */}
      <div
        style={{
          position: 'absolute',
          inset: 0,
          backgroundImage:
            'radial-gradient(1000px 600px at 70% 50%, rgba(30, 58, 138, 0.3), transparent 70%), radial-gradient(800px 500px at 20% 50%, rgba(255, 85, 51, 0.15), transparent 70%)',
        }}
      />

      <div
        style={{
          display: 'flex',
          width: '100%',
          height: '100%',
          padding: '50px 70px 80px 70px',
          gap: 50,
          alignItems: 'center',
          boxSizing: 'border-box',
        }}
      >
        {/* Left: Mobile Field Guide Scanner PWA */}
        <div
          style={{
            flex: '0 0 330px',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            opacity: scannerT,
            transform: `scale(${scannerScale})`,
          }}
        >
          {/* Real Phone Frame for 390x844 */}
          <div
            style={{
              width: 310,
              height: 670,
              borderRadius: 40,
              border: '8px solid #1e293b',
              boxShadow: '0 25px 60px rgba(0,0,0,0.7), 0 0 35px rgba(16, 185, 129, 0.3)',
              overflow: 'hidden',
              backgroundColor: '#090d16',
              position: 'relative',
            }}
          >
            <Img
              src={staticFile('textures/tix/video_scanner.png')}
              style={{ width: '100%', height: '100%', objectFit: 'cover' }}
            />
          </div>

          <div
            style={{
              marginTop: 14,
              padding: '8px 18px',
              borderRadius: 999,
              background: 'rgba(16, 185, 129, 0.15)',
              border: '1px solid rgba(16, 185, 129, 0.4)',
              color: '#34d399',
              fontSize: 13,
              fontWeight: 800,
              letterSpacing: '0.1em',
              textTransform: 'uppercase',
            }}
          >
            ✓ Risposta Sonora Istantanea (300ms)
          </div>
        </div>

        {/* Right: Vendor Bookings Dashboard & Passenger Manifest */}
        <div
          style={{
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            gap: 16,
            transform: `translateX(${manifestX}px)`,
          }}
        >
          {/* Browser Mockup */}
          <div
            style={{
              borderRadius: 18,
              overflow: 'hidden',
              border: '1px solid rgba(255, 255, 255, 0.15)',
              boxShadow: '0 25px 55px rgba(0,0,0,0.6)',
              backgroundColor: '#0f172a',
            }}
          >
            {/* Browser Header */}
            <div
              style={{
                height: 38,
                background: '#1e293b',
                display: 'flex',
                alignItems: 'center',
                padding: '0 16px',
                gap: 8,
              }}
            >
              <span style={{ width: 11, height: 11, borderRadius: '50%', background: '#ef4444' }} />
              <span style={{ width: 11, height: 11, borderRadius: '50%', background: '#eab308' }} />
              <span style={{ width: 11, height: 11, borderRadius: '50%', background: '#22c55e' }} />
              <span style={{ color: '#94a3b8', fontSize: 13, marginLeft: 16, fontFamily: 'monospace' }}>
                tixetours.com/vendor/bookings
              </span>
            </div>

            <div style={{ height: 490, overflow: 'hidden' }}>
              <Img
                src={staticFile('textures/tix/video_manifest.png')}
                style={{ width: '100%', height: 'auto', display: 'block' }}
              />
            </div>
          </div>

          {/* Key Capabilities Badges */}
          <div
            style={{
              display: 'flex',
              gap: 16,
              opacity: badge1T,
            }}
          >
            <div
              style={{
                flex: 1,
                background: 'rgba(15, 23, 42, 0.88)',
                border: '1px solid rgba(255, 85, 51, 0.4)',
                borderRadius: 14,
                padding: '12px 18px',
              }}
            >
              <div style={{ color: '#ff7755', fontSize: 12, fontWeight: 800, textTransform: 'uppercase' }}>
                Presenze con 1-Click
              </div>
              <div style={{ color: '#ffffff', fontSize: 15, fontWeight: 700, marginTop: 4 }}>
                [✓ Presente] [⏱ Ritardo] [✖ No-Show]
              </div>
            </div>

            <div
              style={{
                flex: 1,
                background: 'rgba(15, 23, 42, 0.88)',
                border: '1px solid rgba(16, 185, 129, 0.4)',
                borderRadius: 14,
                padding: '12px 18px',
              }}
            >
              <div style={{ color: '#34d399', fontSize: 12, fontWeight: 800, textTransform: 'uppercase' }}>
                Manifesto Ufficiale
              </div>
              <div style={{ color: '#ffffff', fontSize: 15, fontWeight: 700, marginTop: 4 }}>
                Export PDF, CSV & Excel per Autorità
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Cinematic Caption */}
      <div
        style={{
          position: 'absolute',
          bottom: 30,
          left: '50%',
          transform: 'translateX(-50%)',
          background: 'rgba(11, 17, 32, 0.94)',
          border: '1px solid rgba(255, 255, 255, 0.15)',
          borderRadius: 12,
          padding: '10px 26px',
          display: 'flex',
          alignItems: 'center',
          gap: 12,
          color: '#ffffff',
          fontFamily: 'Inter, system-ui, -apple-system, sans-serif',
          fontSize: 17,
          fontWeight: 700,
          letterSpacing: '0.14em',
          textTransform: 'uppercase',
          boxShadow: '0 10px 30px rgba(0,0,0,0.5)',
        }}
      >
        <span style={{ width: 8, height: 8, borderRadius: 2, backgroundColor: '#ff5533' }} />
        <span>CONFORMITÀ OPERATIVA GUIDE & PORTALE FORNITORI AVANZATO</span>
      </div>
    </AbsoluteFill>
  );
};
