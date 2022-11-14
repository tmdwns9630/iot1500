import ChatBot from "react-simple-chatbot";
import { ThemeProvider } from "styled-components";

const chatbot = () => {
  const steps = [
    {
      id: "0",
      message: `갓디노님! 안녕하세요.
           갓디노 블로그 상담 챗봇입니다.`,
      trigger: "1",
    },
    {
      id: "1",
      message: `제 블로그의 서비스가 궁금하셨죠?            
            그럼 소개를 시작해볼까요?
            준비가 되셨다면 시작버튼을
            눌러 주세요.`,
      trigger: "2",
    },
    {
      id: "2",
      options: [{ value: 1, label: "시작하기", trigger: "3" }],
    },
    {
      id: "3",
      message: `블로그와 앱이 연동 되었는지 확인해주시고 연결을 해주세요.`,
      trigger: "4",
    },
    {
      id: "4",
      component: (
        <div>
          <a>돌아가기</a>
          <a>연결하기</a>
        </div>
      ),
    },
    {
      id: "5",
      component: <div>이동</div>,
    },
  ];

  const theme = {
    background: "#f5f8fb",
    fontFamily: "Helvetica Neue",
    headerBgColor: "#EF6C00",
    headerFontColor: "#fff",
    headerFontSize: "15px",
    botBubbleColor: "#F29F05",
    botFontColor: "#FFF",
    userBubbleColor: "#fff",
    userFontColor: "#4a4a4a",
  };

  return (
    <>
      <ThemeProvider theme={theme}>
        <ChatBot
          steps={steps}
          hideHeader={true}
          placeholder={"채팅이 불가능한 채널입니다."}
        />
      </ThemeProvider>
    </>
  );
};

export default chatbot;
